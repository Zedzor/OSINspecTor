import json
import pandas as pd
from requests import get

def get_mx(domain: str) -> dict:

    API = 'https://freeapi.robtex.com/pdns/forward/'

    try:
        data = get(f'{API}{domain}')
        if data.status_code == 200:
            if data.text != '':
                info = [json.loads(entry)
                    for entry in data.text.split("\r\n")
                    if entry != '']
                df = pd.DataFrame(info)[['rrname', 'rrdata', 'rrtype']]
                df = df[df['rrtype']=='MX']
                results = list(df['rrdata'].values)
            else:
                results = "No se encontraron resultados para este dominio."
                data.status_code = 404
        else:
            results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    except:
        results = 'Este servicio no está disponible en este momento:'
        status = 503
    finally:
        return {'results': results, 'status': status}