import json
import requests

def getRev(ip):
	revurl = "https://sonar.omnisint.io/reverse/"+ip
	data = requests.get(revurl)
	status = json.loads(data.text)
	return status