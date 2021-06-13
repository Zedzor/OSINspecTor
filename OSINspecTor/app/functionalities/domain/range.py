from socket import gethostbyname
from  requests import get

def get_range(domain: str) -> dict:

    API = 'https://rest.db.ripe.net/search.json?query-string='
    FLAGS = '&type-filter=inetnum&flags=no-referenced&flags=no-irt&source=RIPE'

    try:
        data = get(f'{API}{gethostbyname(domain)}{FLAGS}')
        if data.status_code == 200:
            json_res = data.json()
            json_res = json_res['objects']['object'][0]
            json_res = json_res['primary-key']['attribute'][0]
            json_res = json_res['value']
            results = json_res
        else:
            results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    except Exception as e:
        results = 'Este servicio no está disponible en este momento:'
        status = 503
    finally:
        return {'results': results, 'status': status}