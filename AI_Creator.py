from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

URL = "https://api.openai.com/v1/chat/completions"

class Bot:
    def __init__(self, model, role, temp, top_p, n = 1, presence_penalty = 0, frequency_penalty = 0):
        self.model = self.set_model(model)
        self.role = self.set_role(role)
        self.temp = self.set_temp(temp)
        self.top_p = self.set_top_p(top_p)
        self.n = self.set_n(n)
        self.presence_penaly = self.set_presence_penalty(presence_penalty)
        self.frequency_penalty = self.set_frequency_penalty(frequency_penalty)
        
    def set_role(self, role):
        valid_roles = ["user", "system", "assistant", ]
        if role in valid_roles:
            return role
        else:
            raise ValueError("Invalid role. Please enter 'system', 'user', or 'assistant'.")
    
    def set_model(self, model):
        valid_models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-32k"]
        if model in valid_models:
            return model.lower()
        else:
            raise ValueError("Invalid model. Please enter 'gpt-3.5-turbo',gpt-4', or 'gpt-4-32k'.")
    
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
    
    def create_content(self, api_key, message):
        payload = {
            "model": self.model,
            "messages": [{"role": self.role, "content": message}],
            "temperature": self.temp,
            "top_p": self.top_p,
            "n": self.n,
            "stream": False,
            "presence_penalty": self.presence_penaly,  
            "frequency_penalty": self.frequency_penalty,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(URL, headers=headers, json=payload, stream=False)
        return response.content.decode('utf-8')

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OpenAI API key not found. Please check your .env file.")
    blog_bot = Bot("gpt-4","System", 0.7, 0.8, 1, 0, 0)
    content = blog_bot.create_content(api_key, "300 word Blog on Orthopedic Bed's Advantages at a 6th grade reading comprehension")
    print(content)
    
if __name__ == "__main__":
    main()
    