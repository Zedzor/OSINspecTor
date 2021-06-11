import requests
def get_vul(dir):
    CONSUMER_KEY = "FrrnWjvV9B3u0Ioi2VjEdIcOgqa9PLDM"
    vulurl = "https://api.shodan.io/shodan/host/"+dir+"?key="+CONSUMER_KEY
    data = requests.get(vulurl)
    if data.status_code == 200:
        info_json=data.json()
        vul_info = {
            'ports': info_json['ports'] if info_json['ports'] is not None else 'Desconocido',   
        }
        return vul_info
    else:
        raise Exception(data.status_code)