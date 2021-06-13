from requests import get
from socket import gethostbyname

def get_range(domain: str) -> dict:

    API = 'https://rest.db.ripe.net/search.json?query-string='
    FLAGS = '&type-filter=inetnum&flags=no-referenced&flags=no-irt&source=RIPE'

    data = get(f'{API}{gethostbyname(domain)}{FLAGS}')
    if data.status_code == 200:
        json_res = data.json()
        json_res = json_res['objects']['object'][0]
        json_res = json_res['primary-key']['attribute'][0]
        json_res = json_res['value']
        results = json_res
        status = 200
    else:
        results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    return {'results': results, 'status': status}