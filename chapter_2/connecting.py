import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
# Ensure the API key is available
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key)


# Example function to query ChatGPT
def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model="gpt-4.1",  # gpt-4 turbo or a model of your preference
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_message}],
        temperature=0.7,
        )       
    return response.choices[0].message.content

def ask_gpt_5(user_message):
    response = client.responses.create(
        model="gpt-5",
        input=user_message,
    )
    return response.output_text

# Example usage
# user = "What is the capital of France?"
# response = ask_chatgpt(user)

# Practice 1
user = "Explain the capital of France."
response = ask_gpt_5(user)
print(response)
