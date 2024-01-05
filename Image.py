import os
import requests
from pexels_api import API
from dotenv import load_dotenv

def download_image(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return True
    return False

def main():
    load_dotenv()
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        raise Exception("Pexels API key not found. Please check your .env file.")

    api = API(api_key)
    query = input("Enter the image query: ")
    output_folder = 'downloaded_images'  # or use a specific folder path

    os.makedirs(output_folder, exist_ok=True)

    api.search(query, results_per_page=1)  # Adjust number of results as needed
    photos = api.get_entries()

    if photos:
        photo = photos[0]  # Getting the first photo
        photo_url = photo.original
        author_name = photo.photographer

        file_name = os.path.basename(photo_url)
        file_path = os.path.join(output_folder, file_name)

        if download_image(photo_url, file_path):
            print(f"Image downloaded: {file_path}")
            print(f"Photo URL: {photo_url}")
            print(f"Author Name: {author_name}")
        else:
            print("Failed to download image.")

if __name__ == '__main__':
    main()
