import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def simple_test():
    try:
        client = openai.OpenAI()  # <--- New OpenAI client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say hello to me in one sentence."}
            ],
            temperature=0.2,
            max_tokens=50
        )
        print("✅ API Connection Successful!")
        print("Model's Reply:")
        print(response.choices[0].message.content)
    except Exception as e:
        print("❌ Something went wrong:")
        print(e)

if __name__ == "__main__":
    simple_test()
