import requests
from bs4 import BeautifulSoup
import urllib.request
import re

def search_ddg_images(query, save_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    # Use Yahoo image search, it's easier to scrape
    url = f"https://images.search.yahoo.com/search/images?p={urllib.parse.quote(query)}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    img_tags = soup.find_all('img')
    for img in img_tags:
        src = img.get('src')
        if src and src.startswith('https://tse'):
            print(f"Downloading from {src}")
            urllib.request.urlretrieve(src, save_path)
            return True
        elif img.get('data-src') and img.get('data-src').startswith('https://tse'):
            src = img.get('data-src')
            print(f"Downloading from {src}")
            urllib.request.urlretrieve(src, save_path)
            return True
            
    print(f"Failed for {query}")
    return False

search_ddg_images("bolsa de couro de tilápia", "brainz_bag.jpg")
search_ddg_images("sapato de couro de tilápia", "brainz_shoes.jpg")
