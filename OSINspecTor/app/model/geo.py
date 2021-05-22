import json
import requests

def get_geo(dominio):
    CONSUMER_KEY = "1238e7183b2c121459bf1c32536954e8"
    geourl = "http://api.ipstack.com/"+dominio+"?access_key="+CONSUMER_KEY
    data = requests.get(geourl)
    status = json.loads(data.text)
    return status