import json
import re
from urllib.parse import urlparse

import requests
from vt import url_id

with open('creds.txt', 'r') as file:
    API_KEY = file.read().splitlines()[1]


def analyse(request_url: str) -> str:
    try:
        analyses = "https://www.virustotal.com/api/v3/analyses/"
        headers_analyses = {
            "accept": "application/json",
            "x-apikey": API_KEY
        }
        to_search = analyses + url_id(request_url)
        print(to_search)
        with requests.get(to_search, headers=headers_analyses) as res:
            loaded_result = json.loads(res.content)
        return loaded_result["data"]["attributes"]['stats']

    except Exception as e:
        print("Error analysing ->", e)
        return "Couldn't analyse the URL."


def get_response(user_input: str) -> str:
    pattern = r'<(https?://[^>\s]+)>|\[(?:[^\]]+)\]\(\s*(https?://[^\s)]+)\s*\)|\b(https?://[^\s)]+)'
    matches = re.findall(pattern, user_input)
    links = [urlparse(url).geturl() for match in matches for url in match if url]
    if links:
        responses: list = []
        for link in links:
            print(link)
            responses.append(analyse(link))
        return f'URL detected. The info about the URL is: {responses}'
    return ''


def get_edited_response(user_input_after: str) -> str:
    response: str = get_response(user_input_after)
    if response != '':
        return "Message Edited. " + response
    return ''
