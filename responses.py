import json
import os
import re
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def _analyse(request_url: str) -> dict | str:
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
            loaded_result = json.loads(res.content)["data"]["attributes"]["stats"]
        if loaded_result["malicious"] > 0 or loaded_result["suspicious"] > 0:
            return loaded_result
        return ''
    except Exception as e:
        print("Error analysing ->", e)
        return "Couldn't analyse the URL."


def get_response(user_input: str) -> str:
    pattern: str = r'<(https?://[^>\s]+)>|\[(?:[^\]]+)\]\(\s*(https?://[^\s)]+)\s*\)|\b(https?://[^\s)]+)'
    matches = re.findall(pattern, user_input)
    links = [urlparse(url).geturl() for match in matches for url in match if url]
    if not links:
        return ''
    responses: list = []
    for link in links:
        res: dict = _analyse(link)
        if res:
            del res['timeout']
            responses.append(res)
    return f'Suspicious URL detected. The info about the URL is: {responses}' if responses else ''


def get_edited_response(user_input_after: str) -> str:
    responses: str = get_response(user_input_after)
    return "Message Edited. " + responses if responses else ''
