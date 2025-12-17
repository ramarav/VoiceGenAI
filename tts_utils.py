# tts_utils.py
import os
import io
import time
from huggingface_hub import InferenceApi
import requests
from dotenv import load_dotenv
import soundfile as sf

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
DEFAULT_MODEL = os.getenv("HF_TTS_MODEL", "facebook/mms-tts-eng")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "samples")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def synthesize_hf_inference(text: str, model: str = DEFAULT_MODEL, voice: str | None = None, **kwargs) -> bytes:
    """
    Use Hugging Face Inference API to synthesize speech.
    Returns raw audio bytes (wav or mp3 depending on model).
    """
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN not set. Put your token in environment / .env file.")

    # Build InferenceApi instance
    inference = InferenceApi(repo_id=model, token=HF_TOKEN)
    params = {}
    if voice:
        params["voice"] = voice
    # Additional parameters can be passed through kwargs
    params.update(kwargs)

    # Many TTS models expect inputs as plain text and return bytes
    result = inference(inputs=text, parameters=params, request_timeout=60)
    # result can be bytes or dict. In many cases huggingface_hub will return bytes for audio.
    if isinstance(result, (bytes, bytearray)):
        return bytes(result)
    # If result is a dict and contains 'audio', 'data' etc. try to handle known formats:
    if isinstance(result, dict):
        # Some endpoints return base64 encoded data or url
        if "audio" in result:
            data = result["audio"]
            if isinstance(data, (bytes, bytearray)):
                return bytes(data)
            # else if base64, decode
            import base64
            return base64.b64decode(data)
        if "wav" in result:
            return result["wav"]
    # fallback: try to request via REST directly (some models may require different endpoints)
    # Attempt direct REST call:
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {"inputs": text, "parameters": params}
    r = requests.post(url, headers=headers, json=payload, stream=True, timeout=120)
    r.raise_for_status()
    return r.content

def save_audio_bytes(audio_bytes: bytes, out_path: str):
    """
    Save raw audio bytes to out_path.
    If bytes are already a complete file (wav/mp3), just write.
    """
    with open(out_path, "wb") as f:
        f.write(audio_bytes)

def synthesize_and_save(text: str, model: str = DEFAULT_MODEL, out_filename: str | None = None, **kwargs) -> str:
    """
    Convenience: synthesize via HF and save to OUTPUT_DIR. Returns filepath.
    """
    audio_bytes = synthesize_hf_inference(text=text, model=model, **kwargs)
    timestamp = int(time.time())
    if out_filename:
        fname = out_filename
    else:
        fname = f"tts_{timestamp}.wav"
    fp = os.path.join(OUTPUT_DIR, fname)
    # try to detect if returned is wav; we'll try to write bytes and rely on format detection
    save_audio_bytes(audio_bytes, fp)
    return fp

# ---- Optional local TTS (skeleton): ----
def synthesize_local_tts(text: str, model_name: str = "tts_models/en/ljspeech/tacotron2-DDC", out_fp: str | None = None) -> str:
    """
    Synthesize using installed local TTS (Coqui TTS). This requires TTS installed and models downloaded.
    This function is optional and will error if TTS library isn't installed.
    """
    try:
        from TTS.api import TTS
    except Exception as e:
        raise RuntimeError("Local TTS not available. Install 'TTS' package to use local synthesis.") from e

    # Example: model_name could be "tts_models/en/ljspeech/tacotron2-DDC"
    tts = TTS(model_name)
    if not out_fp:
        out_fp = os.path.join(OUTPUT_DIR, f"local_tts_{int(time.time())}.wav")
    tts.tts_to_file(text=text, file_path=out_fp)
    return out_fp
