import AI_Creator as AI
from datetime import date
import Product as Prod



class WrittenWord():
    def __init__(self, product, type, word_limit, reading_comprehension):
        self.product = product
        self.type = self.set_type(type)
        self.word_limit = self.set_word_limit(word_limit)
        self.reading_comprehension = self.set_reading_comprehension(reading_comprehension)
        
    def get_type(self):
        return self.type
    
    def get_word_limit(self):
        return self.word_limit
    
    def get_reading_comprehension(self):
        return self.reading_comprehension
    
    def set_type(self, type):
        valid_types = ["Blog", "Book", "Article"]
        if type in valid_types:
            return type
        else:
            raise ValueError("Invalid type. Please enter 'Blog', 'Book', or 'Article'.")
            
    def set_word_limit(self, word_limit):
        if self.type == "Blog" and 500 <= word_limit <= 2500:
            return word_limit
        elif self.type == "Article" and 6000 <= word_limit <= 10000:
            return word_limit
        elif self.type == "Book" and 40000 <= word_limit <= 110000:
            return word_limit
        else:
            raise ValueError("Invalid word limit for the chosen type.")
    
    def set_reading_comprehension(self, reading_comprehension):
        valid_grades = ["7th Grade", "8th Grade", "9th Grade"]
        if reading_comprehension in valid_grades:
            return reading_comprehension
        else:
            raise ValueError("Invalid reading comprehension level. Please choose among '7th Grade', '8th Grade', or '9th Grade'.")
        
class Blog(WrittenWord):
    def __init__(self, headline, banner, content_goal, overview, conclusion, keywords):
        self.headline = headline
        self.banner = banner
        self.content_goal = content_goal
        self.overview = overview
        self.conclusion = conclusion
        self.keywords = keywords
        
    def get_headline(self):
        return self.headline
    
    def get_banner(self):
        return self.banner
    
    def get_content_goal(self):
        return self.content_goal
    
    def get_overview(self):
        return self.overview
    
    def get_conclusion(self):
        return self.conclusion
    
    def get_keywords(self):
        return self.keywords
    
    def set_headline(self, headline):
        if 6 <=len(headline) <= 11:
            return headline
        else:
            raise ValueError("Headline should be between 6 and 11 words.")
        
    def set_banner(self, banner):
        return self.banner
        
    def set_content_goal(self, goal):
        valid_goals = ["Traffic", "SEO", "Brand"]
        if goal in valid_goals:
            return goal
        else:
            raise ValueError("Invalid content goal. Please choose among 'Traffic', 'SEO', or 'Brand'.")
    
    def set_overview(self, overview):
        return overview
    
    def set_conclusion(self, conclusion):
        return conclusion
    
    def set_keywords(self, keywords):
        if 2 <= len(keywords) <= 5:
            return keywords
        else:
            raise ValueError("Keywords should be between 2 and 5 words.")
        
class List_Blog():
    def __init__(self, blog_list):
        self.blog_list = blog_list

class Case_Study_Blog():
    def __init__(self, case_study):
        self.case_study = case_study
    
class Tutorial_Blog():
    def __init__(self, tutorial):
        self.tutorial = tutorial
    

def main():
    try:
        ortho_bed = Prod("Ortho Bed", "Orthopedic Bed", 2000, "https://www.ortho-bed.com/")
        pet_hut_ortho_bed = WrittenWord(ortho_bed, "Blog", 500, "7th Grade")

        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
