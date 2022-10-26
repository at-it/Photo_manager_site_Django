import json
import requests


class API():

    def get_json_from_site(url: str) -> json:
        api_response = requests.get(url)
        data = api_response.text
        parse_json = json.loads(data)
        return parse_json
