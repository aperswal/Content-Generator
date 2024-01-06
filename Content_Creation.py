import re
import os
import requests
from pexels_api import API
from dotenv import load_dotenv
import AI_Creator as AI
import Product as Prod

URL = "https://api.openai.com/v1/chat/completions"
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("OpenAI API key not found. Please check your .env file.")

class Content_Creation:
    def __init__(self, product, bot):
        self.blog_bot = bot
        self.product = product
        self.conversation_history = []
        
    def create():
        product = input("Enter the name of the product: ")
        description = input("Enter the description of the product: ")
        price = int(input("Enter the price of the product: $"))
        link = input("Enter the link of the product: ")
        length = input("Enter the number of items in the blog: ")
        blog_bot = AI.Bot("gpt-3.5-turbo", "assistant", 0.7, 0.8, 1, 0, 0)
        sell = Prod.Product({product}, {description}, {price}, {link})
        blog = ""
        
        conversation_history = []
        
        headline_message = f"Generate a catchy and concise blog headline, within 6 to 11 words, focusing on a list of {length} related items or alternatives. One of these items should be closely associated with or similar to '{sell.product_description}'. The headline should be engaging and tailored to highlight the unique features of these items, enticing readers to learn more about them, particularly the affiliate product."
        headline = blog_bot.create_content(api_key, headline_message, conversation_history)
        blog += headline

        banner_message = f"Write a search query that is 5 words and simple that would display return andimage for this blog that would be supportive of the headline and target the key demographic, and format it as *** query *** because I will use code to extract the query using regex then, make sure to query it as you would as a human into pexels so for example just listing the item name or a simple search without the word image in the query since you are already in a image directory when searching, MAKE SURE IT IS 5 WORDS AND SURROUNDED BY *** query ***"
        banner = blog_bot.create_content(api_key, banner_message, conversation_history)
        
        blog += "\n" + banner + "\n"

        topic_overview_message = f"Write an overview of the topic that would be about 3 - 4 sentences, narrative based showing that you are part of the key demographic, make the introduction to the topic interesting and have a hook so people want to keep reading."
        topic_overview = blog_bot.create_content(api_key, topic_overview_message, conversation_history)
        blog += topic_overview
        
        covered_content_message = f"Name the specific things you will cover in this blog in the following format, only give the names: and seperate them by a comma and all in one line I will be splitting this later in my code with .split(', ') so make it accomodating for that"
        covered_content = blog_bot.create_content(api_key, covered_content_message, conversation_history)
        list_items = covered_content.split(", ")
        
        for item in list_items:
            blog += "\n" + "Topic: " + item + "\n"
            
            introduction_message = f"create an introduction of the {item} that would be 2 - 3 sentences"
            introduction = blog_bot.create_content(api_key, introduction_message, conversation_history)
            blog += introduction
            
            image_message = f"create an image of the {item} that would be a search query, similar to the banner and format it as *** query *** because I will use code to extract the query using regex then, make sure to query it as you would as a human into pexels so for example just listing the item name or a simple search without the word image in the query since you are already in a image directory when searching, MAKE SURE IT IS 5 WORDS AND SURROUNDED BY *** query ***"
            image = blog_bot.create_content(api_key, image_message, conversation_history)
            blog += "\n" + image + "\n"
            
            logic_message = f"create a logical paragraph analysis of the {item} that would be 4 - 5 sentences"
            logic = blog_bot.create_content(api_key, logic_message, conversation_history)
            blog += logic
            
            emotional_message = f"create a logical paragraph analysis of the {item} that would be 2 - 3 sentences"
            emotion = blog_bot.create_content(api_key, emotional_message, conversation_history)
            blog += "\n" + emotion + "\n"
            
            cta_message = f"create a call to action for the {item} that would be 1 sentence, it should in the cta have a magnetic reason why they should buy, acknowledge the avatar that would be buying it, give them a goal, show them time running out and end with a container phrase that can be focused on rhyme or alliteration"
            cta = blog_bot.create_content(api_key, cta_message, conversation_history)
            blog += cta + "\n"
            
        conclusion_message = f"create a conclusion of the blog that would be 2 - 3 sentences"
        conclusion = blog_bot.create_content(api_key, conclusion_message, conversation_history)
        blog += "\n" + conclusion
        
        return blog
        
    if __name__ == "__main__":
        create()