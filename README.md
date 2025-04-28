

# 🤖 Zero-Shot LLM Task Pipeline

Built an end-to-end **Zero-Shot Learning Text Inference App** using **Streamlit** and **OpenAI GPT models (GPT-3.5-turbo / GPT-4)**.

This application enables users to dynamically perform multiple natural language tasks — **Summarization**, **Translation**, **Question Generation**, and **Sentiment Analysis** — by simply providing input text without any additional training.

---

## 🚀 Live Demo
👉 [Visit Live App Here](https://zero-shot-llm-pipeline-s7qsz4b4chypyjrhrcapprk.streamlit.app)

---

## 📚 Features

- 🔹 **Dynamic Zero-shot Prompting** for various NLP tasks
- 🔹 **Model Switching** (choose between GPT-3.5-turbo and GPT-4)
- 🔹 **Task-specific Example Auto-fill** to make testing faster
- 🔹 **Real-time Response Time Measurement**
- 🔹 **Approximate Token Usage Estimation**
- 🔹 **Clean UI** with Spinner Loading and Input Clearing
- 🔹 **Deployed** on **Streamlit Community Cloud**

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **LLM API:** OpenAI GPT-3.5-turbo / GPT-4
- **Prompt Engineering:** Zero-shot Dynamic Prompt Templates
- **Deployment:** Streamlit Community Cloud
- **Version Control:** Git, GitHub

---

## 🖥️ How It Works

1. Choose a **task** (Summarization, Translation, Question Generation, Sentiment Analysis)
2. Enter your **text** or auto-fill from provided examples
3. Select the **model** (GPT-3.5 or GPT-4)
4. Run the task and view:
   - Generated output
   - Selected model and task details
   - Response time
   - Approximate token usage

---

## 📦 Local Setup Instructions

Want to run this project locally?  
Follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zero-shot-llm-pipeline.git
cd zero-shot-llm-pipeline
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variable

Create a `.env` file inside the root directory:

```plaintext
OPENAI_API_KEY=your-openai-api-key-here
```

(Or set the OpenAI API key manually inside the code for testing.)

### 5. Run Streamlit App

```bash
streamlit run src/app_streamlit.py
```

✅ Your app will launch at `http://localhost:8501`.

---

## ✨ Future Enhancements

- Add **Few-Shot Learning** capabilities (example-augmented prompts)
- Deploy **backend FastAPI server** separately for scalable architectures
- Integrate **multiple LLM providers** (Anthropic Claude, Google Gemini, etc.)
- Implement **user authentication** for managing API costs

---

## 📄 License

This project is licensed under the MIT License - feel free to modify and use it!

---

# 📢 Credits

Special thanks to the open-source community and OpenAI APIs for powering the backend intelligence behind this project!

Built with 💻, 🚀, and a lot of ☕️.

---

# 🎯 Project Snapshot

| Component | Status |
|:----------|:-------|
| Working Frontend (Streamlit) | ✅ |
| LLM Model Switching (3.5/4.0) | ✅ |
| Deployment to Streamlit Cloud | ✅ |
| Token Usage Tracking | ✅ |
| Resume-Portfolio Ready | 🔥 |

---

# 🔥 Final Note:

If you like this project, feel free to ⭐️ the repository and connect!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/your-linkedin-profile)

---
