import Product as Prod
import WrittenWord as WW
import AI_Creator as AI
import Content_Creation as CC
import regex as re
import Image as Img
from docx import Document
from docx.shared import Inches

document = Document()
style = document.styles['Normal']
style.font.name = 'Calibri'


def main():
    blog = CC.Content_Creation.create()
    print(blog)
    
    image_queries = re.findall(r'\*\*\*\s*(.+?)\s*\*\*\*', blog)
    headline = re.search(r'"(.*?)"', blog)
    headline = headline.group(1)
    print(headline)
    topics = re.findall(r"Topic:\s*(.*?)\n", blog, re.IGNORECASE)
    print(topics)
    # for query in image_queries:
    #     Img.download(query)
        
    document.add_heading(headline, 0)
    
    document.save('demo.docx')
    
    
            

if __name__ == "__main__":
    main()
    
    
    
    
""" image_queries = re.findall(r'\*\*\* (.+?) \*\*\*', blog)

        image_info = []

        for query in image_queries:
            pexels_api.search(query, results_per_page=1)
            photos = pexels_api.get_entries()

            if photos:
                photo = photos[0]
                photo_url = photo.original
                author_name = photo.photographer

                file_name = os.path.basename(photo_url)
                file_path = os.path.join('downloaded_images', file_name)
                os.makedirs('downloaded_images', exist_ok=True)

                if download_image(photo_url, file_path):
                    print(f"Image downloaded: {file_path}")
                    image_info.append({'url': photo_url, 'author': author_name, 'file_path': file_path})
                else:
                    print("Failed to download image.")

        # Print the image details
        for info in image_info:
            print(f"Image URL: {info['url']}, Author: {info['author']}, File Path: {info['file_path']}") """