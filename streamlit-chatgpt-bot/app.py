import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file if available
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="ChatGPT AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Configuration
st.sidebar.title("⚙️ Configuration")

# API Key input (defaults to env variable if present)
env_api_key = os.getenv("OPENAI_API_KEY", "")
api_key = st.sidebar.text_input(
    "OpenAI API Key",
    value=env_api_key,
    type="password",
    help="Enter your OpenAI API key (starts with sk-...). You can also set OPENAI_API_KEY in a .env file."
)

st.sidebar.divider()

# Model selection
model_options = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"]
selected_model = st.sidebar.selectbox(
    "Select Model",
    options=model_options,
    index=0,
    help="gpt-4o is OpenAI's flagship smart model. gpt-4o-mini is fast and lightweight."
)

# System Prompt setting
system_prompt = st.sidebar.text_area(
    "System Persona Prompt",
    value="You are a helpful, friendly, and knowledgeable AI assistant.",
    height=100,
    help="Define how the AI chatbot should behave."
)

# Advanced Hyperparameters
st.sidebar.subheader("Hyperparameters")
temperature = st.sidebar.slider(
    "Temperature (Creativity)",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1,
    help="Higher values make output more random, lower values make it more deterministic."
)

max_tokens = st.sidebar.slider(
    "Max Output Tokens",
    min_value=100,
    max_value=4096,
    value=1000,
    step=100
)

# Clear chat history button
if st.sidebar.button("🗑️ Clear Chat History", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

# Header
st.title("🤖 ChatGPT Assistant")
st.caption("Powered by OpenAI API & Streamlit")

# API Key validation check
if not api_key:
    st.warning("⚠️ Please provide an OpenAI API Key in the sidebar or set `OPENAI_API_KEY` in your environment/.env file to start chatting.")
    st.info("💡 Don't have a key? Get one at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize Chat Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box
if prompt := st.chat_input("Ask ChatGPT anything..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Render user message immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare complete message list with system prompt
    api_messages = [{"role": "system", "content": system_prompt}] + [
        {"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages
    ]

    # Generate assistant streaming response
    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=selected_model,
                messages=api_messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True
            )

            # Define generator for st.write_stream
            def stream_generator():
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content

            response_content = st.write_stream(stream_generator())

            # Save assistant message to session state
            st.session_state.messages.append({"role": "assistant", "content": response_content})

        except Exception as e:
            st.error(f"❌ OpenAI API Error: {str(e)}")
