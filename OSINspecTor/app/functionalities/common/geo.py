import requests
from flag import flag
from django.http.response import JsonResponse

def get_geo(dir: str) -> JsonResponse:

    def quitar_nulos(foo):
        return foo if foo is not None else 'Desconocido'

    def bandera(foo):
        return flag(foo) if foo is not None else '😔🤟'

    API = 'http://api.ipstack.com/'
    CONSUMER_KEY = '1238e7183b2c121459bf1c32536954e8'
    
    try:
        data = requests.get(f'{API}{dir}?access_key={CONSUMER_KEY}')
        code = data.status_code
        if code == 200:
            info_json = data.json()
            geo_info = {
                'latitude': quitar_nulos(info_json['latitude']),
                'longitude': quitar_nulos(info_json['longitude']),
                'city': quitar_nulos(info_json['city']),
                'region': quitar_nulos(info_json['region_name']),
                'country': quitar_nulos(info_json['country_name']),
                'flag': bandera(info_json['country_code']),  
            }
            response = JsonResponse({'results': geo_info})
        else:
            response = JsonResponse({'results': f'Error: {code}'}, status=code)
    except Exception as e:
        msg = 'Este servicio no está disponible en este momento:'
        response = JsonResponse({'results': f'{msg} {e}'}, status=503)
    finally:
        return response