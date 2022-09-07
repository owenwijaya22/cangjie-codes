import requests
import json

urls = [
    "https://edwag.github.io/js/cj5-tc.min.json",
    "https://edwag.github.io/js/cj5-tc.min.json"
]

headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,id;q=0.8"
}


def fetch_response(url):
    response = requests.get(url, headers=headers).json()
    return response


for index, url in enumerate(urls):
    with open(f'./data/{index}.json', 'w', encoding='utf-8') as file:
        response = fetch_response(url)
        json.dump(response, file, ensure_ascii=False, indent=4)
