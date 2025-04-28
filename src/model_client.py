# src/model_client.py

import openai
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# New OpenAI v1.x style
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Send prompt to OpenAI LLM and get the reply."""
    client = openai.OpenAI()  # create client first
    response = client.chat.completions.create(
        model=model,  # Use whichever model you prefer
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500,
    )
    return response.choices[0].message.content
