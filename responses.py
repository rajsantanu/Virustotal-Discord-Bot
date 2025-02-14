import json
import re
from urllib.parse import urlparse

import requests

with open('creds.txt', 'r') as file:
    API_KEY: str = file.read().splitlines()[1]


def analyse(request_url: str) -> str:
    try:
        url: str = "https://www.virustotal.com/api/v3/urls"
        analyses: str = "https://www.virustotal.com/api/v3/analyses/"

        payload: dict = {"url": request_url}
        headers_url: dict = {
            "accept": "application/json",
            "x-apikey": API_KEY,
            "content-type": "application/x-www-form-urlencoded"
        }
        headers_analyses: dict = {
            "accept": "application/json",
            "x-apikey": API_KEY
        }

        with requests.post(url, data=payload, headers=headers_url) as req:
            url_id = json.loads(req.content)["data"]["id"]
        with requests.get(analyses + url_id, headers=headers_analyses) as res:
            loaded_result = json.loads(res.content)
        return loaded_result["data"]["attributes"]["stats"]

    except Exception as e:
        print("Error analysing ->", e)
        return "Couldn't analyse the URL."


def get_response(user_input: str) -> str:
    pattern: str = r'<(https?://[^>\s]+)>|\[(?:[^\]]+)\]\(\s*(https?://[^\s)]+)\s*\)|\b(https?://[^\s)]+)'
    matches = re.findall(pattern, user_input)
    links = [urlparse(url).geturl() for match in matches for url in match if url]
    if links:
        responses: list = []
        for link in links:
            responses.append(analyse(link))
        return f'URL detected. The info about the URL is: {responses}'
    return ''


def get_edited_response(user_input_after: str) -> str:
    response: str = get_response(user_input_after)
    if response != '':
        return "Message Edited. " + response
    return ''
