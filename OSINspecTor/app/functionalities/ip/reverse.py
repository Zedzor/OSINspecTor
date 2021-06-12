import requests
from django.http.response import JsonResponse

def get_reverse(ip: str) -> JsonResponse:

	REVURL = 'https://sonar.omnisint.io/reverse/'

	try:
		data = requests.get(f'{REVURL}{ip}')
		code = data.status_code
		if code == 200:
			response = JsonResponse({'results': data.json()})
		else:
			response = JsonResponse({'results': f"Error: {code}"}, status=code)
	except Exception as e:
		msg = 'Este servicio no está disponible en este momento:'
		response = JsonResponse({'results': f'{msg} {e}'}, status=503)
	finally:
		return response