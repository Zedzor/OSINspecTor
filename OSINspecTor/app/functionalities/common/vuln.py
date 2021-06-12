import requests
from django.http.response import JsonResponse

def get_vulns(dir: str)  -> JsonResponse:

    def quitar_nulos(foo):
        return foo if foo is not None else 'Desconocido'

    API = 'https://api.shodan.io/shodan/host/'
    CONSUMER_KEY = 'FrrnWjvV9B3u0Ioi2VjEdIcOgqa9PLDM'

    try:
        data = requests.get(f'{API}{dir}?key={CONSUMER_KEY}')
        code = data.status_code
        if code == 200:
            info_json = data.json()
            vul_info = {
                'ports': quitar_nulos(info_json['ports']),   
            }
            response = JsonResponse({'results': vul_info})
        else:
            response = JsonResponse({'results': f'Error: {code}'}, status=code)
    except Exception as e:
        msg = 'Este servicio no está disponible en este momento:'
        response = JsonResponse({'results': f'{msg} {e}'}, status=503)
    finally:
        return response
