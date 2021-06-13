from requests import get

def get_vulns(dir: str)  -> dict:

    def quitar_nulos(foo):
        return foo if foo is not None else 'Desconocido'

    API = 'https://api.shodan.io/shodan/host/'
    CONSUMER_KEY = 'FrrnWjvV9B3u0Ioi2VjEdIcOgqa9PLDM'

    try:
        data = get(f'{API}{dir}?key={CONSUMER_KEY}')
        if data.status_code == 200:
            info_json = data.json()
            results = {'ports': quitar_nulos(info_json['ports'])}
        else:
            results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    except Exception as e:
        results = 'Este servicio no está disponible en este momento:'
        status = 503
    finally:
        return {'results': results, 'status': status}
