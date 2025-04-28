# src/app_streamlit.py

import streamlit as st
import requests
import time
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/run_task/"

# Streamlit page setup
st.set_page_config(page_title="Zero-Shot LLM Task Pipeline", page_icon="🤖")

st.title("🤖 Zero-Shot LLM Task Pipeline")
st.caption("Built with FastAPI, Streamlit, and OpenAI • Powered by Dynamic Prompt Engineering")
st.write("Select a task, enter your text, and see the AI-generated output!")

# Sidebar for extra controls
with st.sidebar:
    st.header("Options")
    model = st.selectbox(
    "Choose Model:",
    ("gpt-3.5-turbo", "gpt-4")
    )
    clear_button = st.button("🧹 Clear Input/Output")

# Dropdown menu for task selection
task = st.selectbox(
    "Select Task:",
    ("Summarization", "Translation", "Question Generation", "Sentiment Analysis")
)
# Example texts based on task
examples = {
    "Summarization": "The mitochondrion is the powerhouse of the cell, producing ATP through respiration.",
    "Translation": "Hello, how are you doing today?",
    "Question Generation": "Photosynthesis is the process by which green plants convert sunlight into energy.",
    "Sentiment Analysis": "I absolutely loved the movie. It was fantastic!"
}

default_text = examples.get(task, "")

# Text input box with default example filled in
input_text = st.text_area("Enter Text Here:", value=default_text, height=200)



# Placeholder for result
result_placeholder = st.empty()

# Submit button
# if st.button("Run Task"):
#     if input_text.strip() == "":
#         st.warning("⚠️ Please enter some text first.")
#     else:
#         with st.spinner("Running AI model... Please wait."):
#             start_time = time.time()
#             payload = {
#             "task": task,
#             "input_text": input_text,
#             "model": model
#             }

#             try:
#                 response = requests.post(API_URL, json=payload)
#                 end_time = time.time()

#                 if response.status_code == 200:
#                     result = response.json()['result']
#                     st.success(f"✅ Task '{task}' completed using {model} in {end_time - start_time:.2f} seconds!")
#                     st.markdown(f"**Selected Model:** {model}")
#                     st.markdown(f"**Selected Task:** {task}")
#                     approx_tokens = (len(input_text) + len(result)) // 4
#                     st.info(f"ℹ️ Approximate token usage: {approx_tokens} tokens")
#                     result_placeholder.subheader("Result:")
#                     result_placeholder.write(result)
#                 else:
#                     st.error(f"❌ API Error: {response.status_code}")
#             except Exception as e:
#                 st.error(f"❌ Connection Error: {e}")


if st.button("Run Task"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        with st.spinner("Running AI model... Please wait."):
            start_time = time.time()

            # Build dynamic prompt
            if task == "Summarization":
                prompt = f"Summarize the following text:\n\n{input_text}"
            elif task == "Translation":
                prompt = f"Translate this English text into French:\n\n{input_text}"
            elif task == "Question Generation":
                prompt = f"Generate two questions based on this text:\n\n{input_text}"
            elif task == "Sentiment Analysis":
                prompt = f"Analyze the sentiment (Positive, Negative, Neutral) of this text:\n\n{input_text}"
            else:
                prompt = f"Perform the task '{task}' on this text:\n\n{input_text}"

            try:
                client = openai.OpenAI()
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,
                    max_tokens=500,
                )
                result = response.choices[0].message.content

                end_time = time.time()

                st.success(f"✅ Task '{task}' completed using {model} in {end_time - start_time:.2f} seconds!")
                st.markdown(f"**Selected Model:** {model}")
                st.markdown(f"**Selected Task:** {task}")

                approx_tokens = (len(input_text) + len(result)) // 4
                st.info(f"ℹ️ Approximate token usage: {approx_tokens} tokens")

                result_placeholder.subheader("Result:")
                result_placeholder.write(result)

            except Exception as e:
                st.error(f"❌ Connection Error: {e}")


# Clear input/output if button clicked
if clear_button:
    st.rerun()

