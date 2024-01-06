import Product as Prod
import WrittenWord as WW
import AI_Creator as AI
import Content_Creation as CC
import regex as re
import Image as Img
from docx import Document
from docx.shared import Inches
import os
from os import listdir
from docx.enum.text import WD_ALIGN_PARAGRAPH


document = Document()
folder_dir = r"C:\Users\adity\OneDrive\Desktop\Affill\downloaded_images"

def main():
    current_topic_number = 0
    
    blog = CC.Content_Creation.create()
    print(blog)
    
    # Extract headline
    headline_match = re.search(r'"(.*?)"', blog)
    headline = headline_match.group(1) if headline_match else "Default Headline"

    # Add headline to the document
    document.add_heading(headline, level=0)
        
    # Extract and download banner image
    banner_query = re.search(r'\*\*\*\s*(.+?)\s*\*\*\*', blog)
    print(banner_query)
    if banner_query:
        banner_image_path = Img.download_landscape(banner_query.group(1), folder_dir)  # Download banner image
        if banner_image_path:
            document.add_picture(banner_image_path, width=Inches(6.0), height=Inches(3.0))
            last_paragraph = document.paragraphs[-1] 
            last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
    print(banner_query)
    # Extract banner image query and introduction
    banner_query_end = banner_query.end() if banner_query else 0
    introduction_start = blog.find('Topic:', banner_query_end)
    introduction = blog[banner_query_end:introduction_start].strip() if introduction_start != -1 else ""

    # Add introduction to the document
    document.add_paragraph(introduction)

    # Process each topic
    topic_patterns = re.findall(r"(Topic: .*?)(?=\nTopic: |$)", blog, re.DOTALL)
    for topic_pattern in topic_patterns:
        # Extract topic title and overview
        topic_parts = re.split(r'\*\*\*\s*.+?\s*\*\*\*', topic_pattern)
        topic_title = re.search(r"Topic: (.*?)\n", topic_parts[0])
        overview = topic_parts[0].split('\n', 1)[1] if len(topic_parts[0].split('\n', 1)) > 1 else ""

        # Add topic title and overview to the document
        document.add_heading(topic_title.group(1), level=1)
        
        document.add_paragraph(overview.strip())

        # Extract and download image for this topic
        image_query = re.search(r'\*\*\*\s*(.+?)\s*\*\*\*', topic_pattern)
        print(image_query)
        if image_query:
            topic_image_path = Img.download_medium_square(image_query.group(1), folder_dir)  # Download image
            if topic_image_path:
                document.add_picture(topic_image_path, width=Inches(4.0), height=Inches(4.0))
                last_paragraph = document.paragraphs[-1] 
                last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                
        print(image_query)
        
        # Extract and add content of the topic
        topic_content = re.split(r'\*\*\*\s*.+?\s*\*\*\*', topic_pattern)
        if len(topic_content) > 1:
            document.add_paragraph(topic_content[1].strip())

    # Save the document
    document.save('demo.docx')
    
if __name__ == "__main__":
    main()
