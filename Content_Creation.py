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
    def __init__(self):
        pass

    def main():
        blog_bot = AI.Bot("gpt-4", "User", 0.7, 0.8, 1, 0, 0)
        ortho_bed = WW.Product("Ortho Bed", "Orthopedic Bed for Extra Large Dogs", 2000, "https://www.ortho-bed.com/")
        pet_hut_ortho_bed = WW.WrittenWord(ortho_bed, "Blog", 700, "7th Grade")
        
        
        content = blog_bot.create_content(api_key, f"We need to write a {pet_hut_ortho_bed. type} with atleast {pet_hut_ortho_bed.word_limit} words at a reading comprehension of {pet_hut_ortho_bed.reading_comprehension} to sell {pet_hut_ortho_bed.product.product_name} at ${(pet_hut_ortho_bed.product.product_price):.2f}, write the blog in the following format Headline should be 6 to 11 words and based on a top 3 list format, like 3 best accessories for your large dog, then I want you to give me an ideal banner image in the format of *** Image Details ***, make it so that the banner image can easily be looked up and inputted into the blog and targets the target demographic of the article along with supports the headline, basically give me a 5 word search to copy and paste to find the banner image online. Then give me an introduction that is brief, follows a made up personal annecdote or narrative that is punchy and interesting and lead to a hook. Introduction should be no more than 4 sentences. Then give me a line break then give me the list items in the following manner. Then repeat this for each item in the list for the blog Topic Overview (2 to 3 sentences), Ideal Image details similar to banner surrounded by *** Image 5 word search *** then description of the product, it should be very indepth, 2 paragraphs each, going from emotional to logical and then a call to action, follow this formula for each list item's Call to Action. M-A-G-I-C Naming Formula: Magnetic Reason, Avatar, Goal, Time Interval, Container Word. Examples such as 88% Off 12-Week Bikini Blueprint, 60 Minute Make Your Friends Jealous Model Hair System, Bend Over Pain Free in 42 Days . . . Healing Fast Track. So the call to action, last sentence of that portion of the blog post should be that topic named after MAGIC, I don't want each portion written for me I just want the sentence. The {pet_hut_ortho_bed.product.product_name} is just one of the product we are selling, so make this blog actually informative to users so even if they aren't looking for the product they still read through it so it shouldn't be focused around the {pet_hut_ortho_bed.product.product_name} but one of the list items should be that. Lastly they should not know we are selling these products, we are just affiliates writing a blog post to them")
        
        print(content)

    if __name__ == "__main__":
        main()