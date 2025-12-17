# app.py
import streamlit as st
from dotenv import load_dotenv
import os
from tts_utils import synthesize_and_save, synthesize_local_tts, OUTPUT_DIR
import base64
import time

load_dotenv()

st.set_page_config(page_title="VoiceGenAI — Text to Speech", page_icon="🎤", layout="centered")

st.title("🎤 VoiceGenAI — Text → Speech")
st.caption("Fast demo: Hugging Face Inference API (default) with optional local TTS fallback")

# Sidebar: settings
st.sidebar.header("Settings")
model_choice = st.sidebar.selectbox("TTS Model (Hugging Face)", options=[
    "facebook/mms-tts-eng",
    "espnet/kan-bayashi-ljspeech",
    "tts_models/en/ljspeech/tacotron2-DDC (local optional)"
], index=0)
use_local = model_choice.startswith("tts_models")
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    st.sidebar.warning("HF_TOKEN not found in environment. Put your token in .env or export HF_TOKEN.")

st.sidebar.markdown("**Output options**")
format_choice = st.sidebar.selectbox("Output format (what to save)", ["wav", "mp3"])
st.sidebar.write("Generated files saved to:", OUTPUT_DIR)

# Main UI
col1, col2 = st.columns([3,1])

with col1:
    text_input = st.text_area("Enter text to synthesize", value="Welcome to VoiceGenAI — convert text to realistic speech.", height=180)
    if st.button("Synthesize"):
        if len(text_input.strip()) == 0:
            st.error("Please enter some text.")
        else:
            with st.spinner("Synthesizing..."):
                try:
                    if use_local:
                        # Local TTS path
                        out_fp = synthesize_local_tts(text_input)
                    else:
                        # Use HF Inference API
                        model = model_choice
                        # choose filename
                        fname = f"voicegen_{int(time.time())}.wav"
                        out_fp = synthesize_and_save(text=text_input, model=model, out_filename=fname)
                    st.success(f"Saved ▶ {out_fp}")
                    # Show audio player
                    audio_bytes = open(out_fp, "rb").read()
                    st.audio(audio_bytes)
                    # Offer download link
                    b64 = base64.b64encode(audio_bytes).decode()
                    st.markdown(f"[Download audio file](data:audio/wav;base64,{b64})", unsafe_allow_html=True)
                except Exception as e:
                    st.exception(e)

with col2:
    st.header("Quick presets")
    if st.button("Short Greeting"):
        st.session_state['preset'] = "Hi, this is VoiceGenAI. Have a great day!"
    if st.button("Technical Demo"):
        st.session_state['preset'] = "This is a demo of text-to-speech synthesis for developer workflows."
    if 'preset' in st.session_state:
        st.write("Loaded preset:")
        st.write(st.session_state['preset'])
        st.write("Click Synthesize to generate audio.")

st.markdown("---")
st.info("Notes: For highest quality voices across languages, use the Hugging Face Inference API with a token. Local TTS (coqui) is available as an option but requires installing TTS and model download.")

st.markdown("## Generated files")
import glob
files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*")), key=os.path.getmtime, reverse=True)[:10]
for f in files:
    st.write(f)
    with st.expander("Play & download"):
        audio_bytes = open(f, "rb").read()
        st.audio(audio_bytes)
        b64 = base64.b64encode(audio_bytes).decode()
        st.markdown(f"[Download](data:audio/wav;base64,{b64})", unsafe_allow_html=True)
