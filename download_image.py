import urllib.request
from config import URL, IMAGE_PATH

def download_image(url, image_path):
        urllib.request.urlretrieve(url, image_path)

download_image(URL, IMAGE_PATH)
