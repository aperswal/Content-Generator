import os
import openai
from dotenv import load_dotenv

load_dotenv()

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except ImportError:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = openai

class ContentCreation:
    def __init__(self):
        self.conversation_history = []

    def create_content(self, topic, keywords, section_count, words_per_section, purpose):
        total_words = section_count * words_per_section
        
        sorted_keywords = sorted(keywords, key=lambda k: (k.avg_monthly_searches, {'low': 3, 'medium': 2, 'high': 1}[k.competition.lower()]), reverse=True)
        
        keyword_info = "\n".join([f"- {k.word} (Monthly searches: {k.avg_monthly_searches}, Competition: {k.competition})" for k in sorted_keywords])
        
        prompt = f"""
        Create a compelling, SEO-optimized blog post about {topic} that promotes {purpose}. Use these advanced copywriting principles:

        1. Start with a captivating headline that grabs attention (spend extra time on this).
        2. Use the AIDA (Attention, Interest, Desire, Action) and PAS (Problem, Agitation, Solution) frameworks.
        3. Write in a conversational tone, using simple language (aim for a Hemingway score of 3rd-5th grade).
        4. Incorporate storytelling to engage the reader.
        5. Use short sentences and paragraphs, focusing on one thought at a time.
        6. Create a "slippery slope" effect, making each sentence lead naturally to the next.
        7. Build tension and resolve it multiple times throughout the post.
        8. Use active voice and prune unnecessary words.
        9. Include rhetorical questions and answer them.
        10. Incorporate self-deprecating humor and honesty to build trust.
        11. Use italics sparingly to emphasize key points.
        12. Address potential objections within the content.
        13. Include testimonials or social proof if relevant.
        14. End with a clear, specific call-to-action related to {purpose}.

        Incorporate the following keywords naturally throughout the text, prioritizing those with higher search volume and lower competition:
        {keyword_info}

        The blog should be approximately {total_words} words long and include:
        1. An attention-grabbing headline (15-20 words) that includes the primary keyword
        2. A meta description for SEO (150-160 characters) that includes the primary keyword
        3. An engaging introduction (100-150 words) that presents a problem or pain point
        4. {section_count} main sections, each with:
           - A descriptive subheading that includes a keyword where natural
           - Approximately {words_per_section} words of content
           - Natural incorporation of keywords, ensuring each keyword is used at least once in the article
        5. A conclusion that resolves the tension and includes a clear call-to-action (100-150 words)
        6. A P.S. section that reinforces the main message or offer

        Additional guidelines:
        - Use the primary keyword in the first 100 words
        - Include keywords in alt text for images (use !IMAGE_ALT: keyword! where an image would be appropriate)
        - Create a sense of urgency or FOMO (Fear of Missing Out) where appropriate
        - Use ellipses (...) occasionally to build suspense
        - Start some sentences with "And," "But," or "So" to maintain flow
        - Use phrases in parentheses to add a personal touch

        Format the blog post using Markdown syntax. Use **bold** for subheadings and *italics* for emphasis.
        """

        self.conversation_history.append({"role": "user", "content": prompt})

        try:
            if isinstance(client, openai.OpenAI):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-16k",
                    messages=self.conversation_history,
                    max_tokens=total_words * 2,
                    temperature=0.7
                )
                content = response.choices[0].message.content
            else:
                response = client.ChatCompletion.create(
                    model="gpt-3.5-turbo-16k",
                    messages=self.conversation_history,
                    max_tokens=total_words * 2,
                    temperature=0.7
                )
                content = response.choices[0].message['content']

            self.conversation_history.append({"role": "assistant", "content": content})
            return content
        except Exception as e:
            print(f"Error in content creation: {e}")
            return None

    def extract_meta_description(self, content):
        lines = content.split('\n')
        for line in lines:
            if line.startswith("Meta description:"):
                return line.replace("Meta description:", "").strip()
        return None

    def remove_meta_description(self, content):
        lines = content.split('\n')
        return '\n'.join([line for line in lines if not line.startswith("Meta description:")])