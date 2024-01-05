import AI_Creator as AI
import WrittenWord as WW
import os
from dotenv import load_dotenv

URL = "https://api.openai.com/v1/chat/completions"
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("OpenAI API key not found. Please check your .env file.")

class Content_Creation:
    def __init__(self, images, intro, content, conclusion):
        self.images = images
        self.intro = intro
        self.content = content
        self.conclusion = conclusion
        

    def main():
        blog_bot = AI.Bot("gpt-3.5-turbo", "assistant", 0.7, 0.8, 1, 0, 0)
        ortho_bed = WW.Product("Ortho Bed", "Orthopedic Bed for Extra Large Dogs", 2000, "https://www.ortho-bed.com/")
        blog = ""
        
        conversation_history = []
        
        headline_message = f"create a headline for a blog post that is list based between 6 - 11 words and covers 3 items that would include one {ortho_bed.product_description}, without naming the {ortho_bed.product_name}"
        headline = blog_bot.create_content(api_key, headline_message, conversation_history)
        blog += headline
        print(headline)

        banner_message = f"Write a search query that is 5 words and simple that would display return andimage for this blog that would be supportive of the headline and target the key demographic, and format it as *** query *** because I will use code to extract the query using regex then"
        banner = blog_bot.create_content(api_key, banner_message, conversation_history)
        blog += "\n" + banner + "\n"
        print("\n" + banner + "\n")

        topic_overview_message = f"Write an overview of the topic that would be about 3 - 4 sentences, narrative based showing that you are part of the key demographic, make the introduction to the topic interesting and have a hook so people want to keep reading."
        topic_overview = blog_bot.create_content(api_key, topic_overview_message, conversation_history)
        blog += topic_overview
        print(topic_overview)
        
        covered_content_message = f"Name the specific things you will cover in this blog in the following format, only give the names: item 1, item 2, ... item n and all in one line I will be splitting this later in my code with .split(', ') so make it accomodating for that"
        covered_content = blog_bot.create_content(api_key, covered_content_message, conversation_history)
        list_items = covered_content.split(", ")
        
        for item in list_items:
            blog += "\n" + item + "\n"
            
            print("\n" + item + "\n")
            
            introduction_message = f"create an introduction of the {item} that would be 2 - 3 sentences"
            introduction = blog_bot.create_content(api_key, introduction_message, conversation_history)
            blog += introduction
            print(introduction)
            
            image_message = f"create an image of the {item} that would be a search query, similar to the banner and format it as *** query *** because I will use code to extract the query using regex then"
            image = blog_bot.create_content(api_key, image_message, conversation_history)
            blog += "\n" + image + "\n"
            print("\n" + image + "\n")
            
            logic_message = f"create a logical paragraph analysis of the {item} that would be 4 - 5 sentences"
            logic = blog_bot.create_content(api_key, logic_message, conversation_history)
            blog += logic
            print(logic)
            
            emotional_message = f"create a logical paragraph analysis of the {item} that would be 2 - 3 sentences"
            emotion = blog_bot.create_content(api_key, emotional_message, conversation_history)
            blog += "\n" + emotion + "\n"
            print(emotion)
            
            cta_message = f"create a call to action for the {item} that would be 1 sentence, it should in the cta have a magnetic reason why they should buy, acknowledge the avatar that would be buying it, give them a goal, show them time running out and end with a container phrase that can be focused on rhyme or alliteration"
            cta = blog_bot.create_content(api_key, cta_message, conversation_history)
            blog += cta + "\n"
            print(cta + "\n")
            
        conclusion_message = f"create a conclusion of the blog that would be 2 - 3 sentences"
        conclusion = blog_bot.create_content(api_key, conclusion_message, conversation_history)
        blog += "\n" + conclusion
        print("\n" + conclusion)
        
        print(blog)

    if __name__ == "__main__":
        main()