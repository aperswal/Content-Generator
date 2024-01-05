import AI_Creator as AI
from datetime import date

class Product:
    def __init__(self, product_name, product_description, product_price, product_affiliate_link):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_affiliate_link = product_affiliate_link

class Marketing:
    def __init__(self):
        pass
        
class WrittenWord(Marketing):
    def __init__(self, product, type, word_limit, reading_comprehension):
        super().__init__()
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
    
    def goal(self):
        print(f'We need to write a {self.type} with a word limit of {self.word_limit} at a reading comprehension of {self.reading_comprehension} to sell {self.product.product_name} at ${(self.product.product_price):.2f} to make ${(self.product.product_price * 0.2):.2f}.')
        
class Blog(WrittenWord):
    def __init__(self, headline, banner, content, cta):
        super().__init__()
        self.headline = headline
        self.banner = banner
        self.content = content
        self.cta = cta
    
    def get_headline(self):
        return self.headline
    
    def get_byLine(self):
        return self.byLine
    
    def get_date(self):
        return self.date
    
    def get_banner(self):
        return self.banner
    
    def get_content(self):
        return self.content
    
    def get_cta(self):
        return self.cta
    
    def set_headline(self, headline):
        if 6 <=len(headline) <= 11:
            return headline
        else:
            raise ValueError("Headline should be between 6 and 11 words.")
        
    def set_banner(self, banner):
        self.banner = banner
        
    def set_content(self, content):
        self.content = content
    
    def set_cta(self, cta):
        self.cta = cta

def main():
    try:
        ortho_bed = Product("Ortho Bed", "Orthopedic Bed", 2000, "https://www.ortho-bed.com/")
        pet_hut_ortho_bed = WrittenWord(ortho_bed, "Blog", 500, "7th Grade")
        pet_hut_ortho_bed.goal()
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
