import os
import requests
from pexels_api import API
from dotenv import load_dotenv

def download_image(url, file_path):
    if not os.path.exists(file_path):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return True
    return False

def download(query):
    load_dotenv()
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        raise Exception("Pexels API key not found. Please check your .env file.")

    api = API(api_key)
    output_folder = 'downloaded_images'

    os.makedirs(output_folder, exist_ok=True)

    api.search(query, results_per_page=15)  
    photos = api.get_entries()

    for photo in photos:
        photo_url = photo.original
        author_name = photo.photographer

        file_name = os.path.basename(photo_url)
        file_path = os.path.join(output_folder, file_name)

        if download_image(photo_url, file_path):
            print(f"Image downloaded: {file_path}")
            print(f"Photo URL: {photo_url}")
            print(f"Author Name: {author_name}")
            break  # Stop after downloading the first available image
        else:
            print(f"Image already exists: {file_path}")
            
if __name__ == "__main__":
    queries = ["cat", "large cat", "small cat"]
    for query in queries:
        download(query)
