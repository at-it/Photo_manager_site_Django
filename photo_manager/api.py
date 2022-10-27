import json
import requests


class API():

    def get_json_from_site(site_url: str) -> json:
        api_response = requests.get(site_url)
        data = api_response.text
        parse_json = json.loads(data)
        return parse_json
