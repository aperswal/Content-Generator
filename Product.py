class Product:
    def __init__(self, product_name, product_description, product_price, product_affiliate_link):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_affiliate_link = product_affiliate_link

def main():
    try:
        ortho_bed = Product("Ortho Bed", "Orthopedic Bed", 2000, "https://www.ortho-bed.com/")
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()