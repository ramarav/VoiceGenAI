
# 🎤 VoiceGenAI — Text to Speech with Generative AI

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-app-red)
![HuggingFace](https://img.shields.io/badge/HuggingFace-TTS-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Stars](https://img.shields.io/github/stars/yourusername/VoiceGenAI?style=social)

> **VoiceGenAI** is a modern **Text-to-Speech (TTS) Generative AI application** built using **Hugging Face models** and **Streamlit**, capable of converting text into natural-sounding human speech.

---

## 🚀 Features

✅ Text-to-Speech using state-of-the-art Hugging Face models  
✅ Streamlit-based interactive UI  
✅ Play & download generated audio  
✅ Supports Hugging Face Inference API  
✅ Optional local offline TTS (Coqui TTS)  
✅ Clean, modular, production-ready Python code  
✅ Docker-ready for deployment  

---

## 🧠 Models Used

| Model | Description |
|------|------------|
| `facebook/mms-tts-eng` | High-quality multilingual TTS |
| `espnet/kan-bayashi-ljspeech` | Research-grade neural TTS |
| `Coqui TTS (optional)` | Offline/local speech synthesis |

---

## 🛠 Tech Stack

- **Python 3.9+**
- **Streamlit**
- **Hugging Face Transformers / Inference API**
- **PyTorch**
- **Coqui TTS (optional)**
- **Docker**

---

## 📂 Project Structure

```
VoiceGenAI/
├── app.py
├── tts_utils.py
├── requirements.txt
├── .env.example
├── Dockerfile
├── README.md
└── samples/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/ramarav/VoiceGenAI.git
cd VoiceGenAI
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Hugging Face Token
- Create token: https://huggingface.co/settings/tokens
- Create `.env` file:
```env
HF_TOKEN=hf_your_token_here
```

### 5️⃣ Run the App
```bash
streamlit run app.py
```

Open browser at 👉 **http://localhost:8501**

---

## 🧪 Example Output

🎧 Text:
```
Welcome to VoiceGenAI, your personal text to speech assistant.
```

🔊 Output:
- Natural human-like speech
- Downloadable `.wav` file

---

## 🐳 Docker Support

```bash
docker build -t voicegenai .
docker run -p 8501:8501 --env HF_TOKEN=hf_xxx voicegenai
```

---

## 🌍 Use Cases

- Accessibility tools
- Voice assistants
- AI narration
- Content creation
- Chatbots with voice
- EdTech / E-learning platforms

---

## 📈 Roadmap

- [ ] Multi-voice selection
- [ ] SSML support
- [ ] Batch TTS (CSV upload)
- [ ] Language auto-detection
- [ ] Cloud deployment (AWS/GCP)
- [ ] REST API version

---

## 🤝 Contributing

Contributions are welcome!  
Fork the repo, create a feature branch, and submit a PR 🚀

---

## ⭐ Show Your Support

If you like this project:
- ⭐ Star the repository
- 🍴 Fork it
- 🧑‍💻 Share it with the community

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🔖 Tags

`#GenerativeAI` `#TextToSpeech` `#HuggingFace` `#Streamlit` `#Python`  
`#AIProjects` `#OpenSource` `#MachineLearning` `#DeepLearning` `#VoiceAI`

---

### 👨‍💻 Author

**Mekala Ramarao**  
Python Developer | AI/ML Engineer  
GPU & AI Systems | Open Source Contributor  

--- 

🔥 *Built for engineers and AI enthusiasts.*
