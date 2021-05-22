import json
import requests

def get_subdomains(dominio):
	suburl = "https://sonar.omnisint.io/all/"+dominio
	data = requests.get(suburl)
	status = json.loads(data.text)
	return status
