import Content_Creation as CC
import regex as re
import Image as Img
from docx import Document
from docx.shared import Inches
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH


# Code to Measure time taken by program to execute. 
import time 

# store starting time 
begin = time.time() 

document = Document()
folder_dir = r"C:\Users\adity\OneDrive\Desktop\ContentGen Blog Creator\downloaded_images"

def add_hyperlink(paragraph, text, url):
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id)
    new_run = docx.text.run.Run(docx.oxml.shared.OxmlElement('w:r'), paragraph)
    new_run.text = text
    new_run.font.color.rgb = docx.shared.RGBColor(0, 0, 255)
    new_run.font.underline = True
    hyperlink.append(new_run._element)
    paragraph._p.append(hyperlink)
    return hyperlink


def main():
    
    blog = CC.Content_Creation.create()
    print(blog)
    
    # Extract headline
    headline_match = re.search(r'"(.*?)"', blog)
    headline = headline_match.group(1) if headline_match else "Default Headline"

    # Add headline to the document
    document.add_heading(headline, level=0)
        
    # Extract and download banner image
    banner_query = re.search(r'\*\*\*\s*(.+?)\s*\*\*\*', blog)
    if banner_query:
        banner_info = Img.download_landscape(banner_query.group(1), folder_dir)
        if banner_info[0]:
            document.add_picture(banner_info[0], width=Inches(6.0), height=Inches(3.0))
            last_paragraph = document.paragraphs[-1] 
            last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            last_paragraph = document.add_paragraph()
            last_paragraph = document.paragraphs[-1] 
            last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_hyperlink(last_paragraph, f"Image by {banner_info[2]} through Pexel", banner_info[1])
            
    # Extract banner image query and introduction
    banner_query_end = banner_query.end() if banner_query else 0
    introduction_start = blog.find('Topic:', banner_query_end)
    introduction = blog[banner_query_end:introduction_start].strip() if introduction_start != -1 else ""
    document.add_paragraph(introduction)


    # Process each topic
    topic_patterns = re.findall(r"(Topic: .*?)(?=\nTopic: |$)", blog, re.DOTALL)
    for topic_pattern in topic_patterns:
        # Extract topic title and overview
        topic_parts = re.split(r'\*\*\*\s*.+?\s*\*\*\*', topic_pattern)
        topic_title = re.search(r"Topic: (.*?)\n", topic_parts[0])
        overview = topic_parts[0].split('\n', 1)[1] if len(topic_parts[0].split('\n', 1)) > 1 else ""
        document.add_heading(topic_title.group(1), level=1)
        document.add_paragraph(overview.strip())

        # Extract and download image for this topic
        image_query = re.search(r'\*\*\*\s*(.+?)\s*\*\*\*', topic_pattern)
        if image_query:
            topic_image_info = Img.download_medium_square(image_query.group(1), folder_dir)
            if topic_image_info[0]:
                document.add_picture(topic_image_info[0], width=Inches(4.0), height=Inches(4.0))
                last_paragraph = document.paragraphs[-1] 
                last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                last_paragraph = document.add_paragraph()
                last_paragraph = document.paragraphs[-1] 
                last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_hyperlink(last_paragraph, f"Image by {topic_image_info[2]} through Pexel", topic_image_info[1])
                
        # Extract and add content of the topic
        topic_content = re.split(r'\*\*\*\s*.+?\s*\*\*\*', topic_pattern)
        if len(topic_content) > 1:
            document.add_paragraph(topic_content[1].strip())

    # Save the document
    document.save('demo.docx')
    time.sleep(1) 
    
    # store end time 
    end = time.time() 
    
    # total time taken 
    print(f"Total runtime of the program is {end - begin}") 
    
if __name__ == "__main__":
    main()
