import json
import requests


def get_dns(domain):
    domain_url = "https://freeapi.robtex.com/pdns/forward/"+domain
    response = requests.get(domain_url)
    if response.ok:
        try:
            return json.loads(response.text)
        except ValueError:
            return [json.loads(entry) for entry in response.text.split("\r\n") if entry != '']
    else:
        raise Exception(response.status_code)
