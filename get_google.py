import urllib.request
import re

def get_google_img(query, filename):
    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=isch"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    matches = re.findall(r'src="(https://encrypted-tbn0\.gstatic\.com/images\?q=[^"]+)"', html)
    if len(matches) > 1:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(matches[1], filename)
    elif len(matches) > 0:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(matches[0], filename)
    else:
        print(f"Failed to find images for {query}")

import urllib.parse
get_google_img("bolsa couro de tilapia moda", "brainz_bag.jpg")
get_google_img("sapato masculino couro de tilapia", "brainz_shoes.jpg")
