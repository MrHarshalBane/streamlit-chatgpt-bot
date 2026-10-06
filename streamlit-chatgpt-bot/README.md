# 🤖 ChatGPT Streamlit Chatbot

An interactive, real-time streaming ChatGPT chatbot built with **Python**, **Streamlit**, and the official **OpenAI API**.

---

## ✨ Features

- 💬 **Real-time Streaming Responses**: Smooth, token-by-token streaming UI using `st.write_stream`.
- 🎛️ **Model Selection**: Switch between `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, and `gpt-3.5-turbo`.
- 🎭 **Custom System Prompt / Persona**: Adjust system instructions directly from the sidebar.
- 🎚️ **Hyperparameter Tuning**: Fine-tune output creativity (`temperature`) and max token length.
- 🔑 **Flexible API Key Management**: Enter key via sidebar UI or load automatically from `.env`.
- 🗑️ **Chat History Reset**: One-click reset to start a fresh conversation.

---

## 🚀 Quick Start

### 1. Install Dependencies

Open your terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key (Optional)

Create a `.env` file in the project folder (or copy `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` and set your key:

```env
OPENAI_API_KEY=sk-proj-your_actual_openai_api_key
```

*Note: You can also enter the API key directly in the sidebar of the running app.*

### 3. Run the Streamlit App

Execute the following command to launch the chatbot in your web browser:

```bash
streamlit run app.py
```

The app will launch automatically at `http://localhost:8501`.

---

## 🛠️ Project Structure

```
streamlit-chatgpt-bot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # Documentation
```
