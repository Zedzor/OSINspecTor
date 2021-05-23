import requests

def get_geo(dir):
    CONSUMER_KEY = "1238e7183b2c121459bf1c32536954e8"
    geourl = "http://api.ipstack.com/"+dir+"?access_key="+CONSUMER_KEY
    data = requests.get(geourl)
    if data.status_code == 200:
        info_json=data.json()
        geo_info = {
            'latitude': info_json['latitude'] if info_json['latitude'] is not None else 'Desconocido',
            'longitude':info_json['longitude'] if info_json['longitude'] is not None else 'Desconocido',
            'city': info_json['city'] if info_json['city'] is not None else 'Desconocido',
            'region': info_json['region_name'] if info_json['region_name'] is not None else 'Desconocido',
            'country': info_json['country_name'] if info_json['country_name'] is not None else 'Desconocido',
            'flag': info_json['location']['country_flag_emoji'] if info_json['location']['country_flag_emoji'] is not None else '😞',   
        }
        return geo_info
    else:
        raise Exception(data.status_code)