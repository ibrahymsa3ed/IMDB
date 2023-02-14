import requests
import json


def getLoc(ip):
    url = f"https://ipinfo.io/{ip}/geo"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.text
    resp_dict = json.loads(response_json)
    print(resp_dict["loc"])


getLoc('105.34.110.153')
