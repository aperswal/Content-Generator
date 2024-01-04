from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

class Bot:
    def __init__(self, role):
        self.role = self.set_role(role)
        
    def set_role(self, role):
        return role

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Retrieve the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OpenAI API key not found. Please check your .env file.")

    # Create the OpenAI client with the API key
    client = OpenAI(api_key=api_key)
    message = [{"role": "system", "content" : "You are a copy writer"}]
    chat = client.chat.completions.create(model = "gpt-4", messages = message)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")

if __name__ == "__main__":
    main()
    