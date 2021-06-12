import json
import requests
from django.http import JsonResponse

def get_reverse(ip):
	REVURL = 'https://sonar.omnisint.io/reverse/'
	try:
		data = requests.get(f'{REVURL}{ip}')
		response = JsonResponse({'results':data.json()})
	except Exception as e:
		response = JsonResponse({'results':f'Este servicio no está disponible en este momento: {e}'}, status=503)
	finally:
		return response