import os
import requests
from dotenv import load_dotenv
from pexels_api import API
import time

load_dotenv()

class ImageHandler:
    def __init__(self):
        self.api = API(os.getenv("PEXELS_API_KEY"))
        self.downloaded_urls = set()

    def search_and_download(self, query, image_type='body', max_results=1, max_retries=5):
        orientation = 'landscape' if image_type == 'banner' else 'square'
        page = 1
        downloaded_images = []

        while len(downloaded_images) < max_results and page <= max_retries:
            try:
                self.api.search(query, page=page, results_per_page=10)
                photos = self.api.get_entries()

                for photo in photos:
                    if image_type == 'banner':
                        url = photo.landscape
                    else:
                        url = photo.medium

                    if url not in self.downloaded_urls:
                        image_data = self._download_image(url)
                        if image_data:
                            self.downloaded_urls.add(url)
                            downloaded_images.append({
                                'data': image_data,
                                'photographer': photo.photographer,
                                'url': url
                            })
                            if len(downloaded_images) == max_results:
                                break

                if len(downloaded_images) == max_results:
                    break
                page += 1
                time.sleep(1)  # To avoid hitting API rate limits

            except Exception as e:
                print(f"Error searching for images: {e}")
                time.sleep(1)  # Wait before retrying

        if not downloaded_images:
            print(f"Failed to find suitable images for '{query}' after {max_retries} attempts.")

        return downloaded_images

    def _download_image(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.content
        except Exception as e:
            print(f"Error downloading image: {e}")
        return None