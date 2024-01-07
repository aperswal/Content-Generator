import os
import requests
from dotenv import load_dotenv
from pexelsapi.pexels import Pexels
from datetime import datetime

downloaded_urls = set()

def download_image(url, file_path):
    """
    Downloads an image from a given URL and saves it to the specified file path.
    """
    if not os.path.exists(file_path):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return file_path
    return None

def unique_filename(directory, base_name, extension):
    """
    Generates a unique filename by appending a timestamp.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{base_name}_{timestamp}.{extension}"
    return os.path.join(directory, filename)

def download_landscape(query, directory):
    """
    Downloads a landscape image based on the specified query.
    Returns the file path, image URL, and photographer's name.
    """
    load_dotenv()
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        raise Exception("Pexels API key not found. Please check your .env file.")

    pexel = Pexels(api_key)
    page = 1
    while True:
        search_photos = pexel.search_photos(query=query, orientation='landscape', size='', color='', locale='', page=page, per_page=1)
        if search_photos['photos']:
            photo = search_photos['photos'][0]
            photo_url = photo['src']['landscape']
            photographer_name = photo['photographer']
            if photo_url not in downloaded_urls:
                downloaded_urls.add(photo_url)
                file_path = unique_filename(directory, f"landscape_{query}", "jpg")
                file_path = download_image(photo_url, file_path)
                return file_path, photo_url, photographer_name
        else:
            return None, None, None
        page += 1

def download_medium_square(query, directory):
    """
    Downloads a medium square image based on the specified query.
    Returns the file path, image URL, and photographer's name.
    """
    load_dotenv()
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        raise Exception("Pexels API key not found. Please check your .env file.")

    pexel = Pexels(api_key)
    page = 1
    while True:
        search_photos = pexel.search_photos(query=query, orientation='square', size='medium', color='', locale='', page=page, per_page=1)
        if search_photos['photos']:
            photo = search_photos['photos'][0]
            photo_url = photo['src']['medium']
            photographer_name = photo['photographer']
            if photo_url not in downloaded_urls:
                downloaded_urls.add(photo_url)
                file_path = unique_filename(directory, f"medium_square_{query}", "jpg")
                file_path = download_image(photo_url, file_path)
                return file_path, photo_url, photographer_name
        else:
            return None, None, None
        page += 1

def main():
    # Example query for testing
    query = "ocean"
    # Download a portrait image based on the query
    if download_landscape(query):
        print(f"Portrait image for '{query}' downloaded successfully.")
    else:
        print(f"Failed to download portrait image for '{query}'.")

    # Download a medium square image based on the query
    if download_medium_square(query):
        print(f"Medium square image for '{query}' downloaded successfully.")
    else:
        print(f"Failed to download medium square image for '{query}'.")

if __name__ == "__main__":
    main()
