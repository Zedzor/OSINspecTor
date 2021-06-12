import json
import requests
from django.http import JsonResponse


def get_dns(domain: str) -> JsonResponse:

    API = 'https://freeapi.robtex.com/pdns/forward/'
    
    try:
        data = requests.get(f'{API}{domain}')
        code = data.status_code
        if code == 200 and data.text != '':
            info = [json.loads(entry) for entry in data.text.split("\r\n") if entry != '']
            dnsserv = [r['rrdata'] for r in info if r['rrtype']=='NS']
            response = JsonResponse({'results': dnsserv})
        else:
            response = JsonResponse({'results':f'Error: 404 Not Found'}, status=404)
    except Exception as e:
        msg = 'Este servicio no está disponible en este momento:'
        response = JsonResponse({'results': f'{msg} {e}'}, status=503)
    finally:
        return response
