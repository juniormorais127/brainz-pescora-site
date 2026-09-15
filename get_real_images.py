from duckduckgo_search import DDGS
import urllib.request

def download_real_img(query, filename):
    print(f"Searching: {query}")
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=3)
        for img in results:
            url = img['image']
            print(f"Downloading from {url}")
            try:
                # Add headers to avoid 403 Forbidden
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                urllib.request.urlretrieve(url, filename)
                print("Success.")
                return True
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                pass
    return False

# Specifically searching for bags and shoes made of tilapia leather
download_real_img("bolsa couro de tilapia peixe exótico real", "brainz_bag.jpg")
download_real_img("sapato couro de tilapia peixe", "brainz_shoes.jpg")
