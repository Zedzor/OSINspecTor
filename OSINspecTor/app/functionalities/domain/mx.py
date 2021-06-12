import json
import requests


def get_mx(domain):
    domain_url = "https://freeapi.robtex.com/pdns/forward/"+domain
    response = requests.get(domain_url)
    if response.ok:
        try:
            return json.loads(response.text)
        except ValueError:
            info = [json.loads(entry) for entry in response.text.split("\r\n") if entry != '']
            return [r['rrdata'] for r in info if r['rrtype']=='MX']
    else: 
        raise Exception(response.status_code)