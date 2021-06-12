import json
import requests
from django.http import JsonResponse

def get_reverse(ip):
	REVURL = 'https://sonar.omnisint.io/reverse/'
	try:
		data = requests.get(f'{REVURL}{ip}')
		if data.status_code == 200:
			response = JsonResponse({'results': data.json()})
		else:
			response = JsonResponse({'results': "Error: "}, status=data.status_code)
	except Exception as e:
		response = JsonResponse({'results': f'Este servicio no está disponible en este momento: {e}'}, status=503)
	finally:
		return response