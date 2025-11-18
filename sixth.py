import sys
import requests


def download_url_and_get_all_hrefs(url):
    hrefs = []

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Chyba pri stahovani URL, status code = {response.status_code}")

    html = response.content.decode('utf-8')

    parts = html.split('<a ')
    for part in parts[1:]:
        if 'href="' in part:
            start = part.find('href="') + 6
            end = part.find('"', start)
            if end > start:
                link = part[start:end]
                hrefs.append(link)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        print(hrefs)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")