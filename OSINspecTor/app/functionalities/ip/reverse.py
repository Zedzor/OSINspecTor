from requests import get

def get_reverse(ip: str) -> dict:

    REVURL = 'https://sonar.omnisint.io/reverse/'

    try:
        data = get(f'{REVURL}{ip}')
        if data.status_code == 200:
            results = data.json()
        else:
            results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    except:
        results = 'Este servicio no está disponible en este momento:'
        status = 503
    finally:
        return {'results': results, 'status': status}