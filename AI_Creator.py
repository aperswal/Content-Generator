from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

URL = "https://api.openai.com/v1/chat/completions"

class Bot:
    def __init__(self, model, role, temp, top_p, n=1, presence_penalty=0, frequency_penalty=0, blog_purpose=""):
        self.model = self.set_model(model)
        self.role = self.set_role(role)
        self.temp = self.set_temp(temp)
        self.top_p = self.set_top_p(top_p)
        self.n = self.set_n(n)
        self.presence_penalty = self.set_presence_penalty(presence_penalty)
        self.frequency_penalty = self.set_frequency_penalty(frequency_penalty)
        self.blog_purpose = blog_purpose
        self.system_message = self.create_system_message()

    def create_system_message(self):
        base_message = "You are an informed and exceptional writer. Your writing can be read at a 7th grade reading level and makes the reader feel understood"
        purpose_message = f"The purpose of your writing is to {self.blog_purpose}." if self.blog_purpose else ""
        return {"role": "system", "content": base_message + purpose_message}

        
    def set_role(self, role):
        valid_roles = ["user", "system", "assistant", ]
        if role in valid_roles:
            return role
        else:
            raise ValueError("Invalid role. Please enter 'system', 'user', or 'assistant'.")
    
    def set_model(self, model):
        valid_models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-32k", "gpt-3.5"]
        if model in valid_models:
            return model.lower()
        else:
            raise ValueError("Invalid model. Please enter 'gpt-3.5-turbo',gpt-4','gpt-4-32k' or 'gpt-3.5'.")
    
    def set_temp(self, temp):
        if -1 <= temp <= 1:
            return temp
        else:
            raise ValueError("Invalid temperature. Please enter a value between -1 and 1.")
    
    def set_top_p(self, top_p):
        return top_p
    
    def set_n(self, n):
        return n
    
    def set_presence_penalty(self, penalty):
        return penalty
    
    def set_frequency_penalty(self, penalty):
        return penalty
    
    def create_content(self, api_key, message, conversation_history):
        if not conversation_history or conversation_history[0]['role'] != 'system':
            conversation_history.insert(0, self.system_message)

        conversation_history.append({"role": "user", "content": message})

        payload = {
            "model": self.model,
            "messages": conversation_history, 
            "temperature": self.temp,
            "top_p": self.top_p,
            "n": self.n,
            "stream": False,
            "presence_penalty": self.presence_penalty,
            "frequency_penalty": self.frequency_penalty,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(URL, headers=headers, json=payload, stream=False)
        response_data = response.json()
        assistant_message = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
        conversation_history.append({"role": "assistant", "content": assistant_message})

        return assistant_message

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OpenAI API key not found. Please check your .env file.")
    
    bot = Bot("gpt-4", "assistant", 0.7, 0.8, 1, 0, 0)
    conversation_history = []

    user_message = "Hello, how are you?"
    print("User:", user_message)
    response = bot.create_content(api_key, user_message, conversation_history)
    print("Assistant:", response)

    user_message = "I have a question about Python."
    print("User:", user_message)
    response = bot.create_content(api_key, user_message, conversation_history)
    print("Assistant:", response)

if __name__ == "__main__":
    main()
    