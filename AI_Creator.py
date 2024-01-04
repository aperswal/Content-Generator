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
        valid_roles = ["User", "System", "Assistant", ]
        if role in valid_roles:
            return role.lower()
        else:
            raise ValueError("Invalid role. Please enter 'System', 'User', or 'Assistant'.")
    
    def set_model(self, model):
        return model
    
    def set_temp(self, temp):
        return temp
    
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
    