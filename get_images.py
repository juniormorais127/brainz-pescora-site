import urllib.request
import urllib.parse
import re

def get_ddg_img(query, path):
    print(f"Searching for: {query}")
    req = urllib.request.Request(
        'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(query + ' images'),
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Buscar links de imagens nos resultados do DuckDuckGo HTML
        matches = re.findall(r'//tse\d\.mm\.bing\.net/th\?id=[^\"]+', html)
        if matches:
            url = 'https:' + matches[0]
            print(f"Found: {url}")
            urllib.request.urlretrieve(url, path)
            return True
        else:
            print("No images found.")
    except Exception as e:
        print(f"Error: {e}")
    return False

get_ddg_img('sapato couro de tilapia moda', 'brainz_shoes.jpg')
get_ddg_img('bolsa artesanal couro de tilapia peixe', 'brainz_bag.jpg')
