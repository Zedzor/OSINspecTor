import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def get_subdomains(domain: str) -> dict:

	def get_types_graph(df: pd.DataFrame):
		types = df['type'].value_counts()
		plt.pie(types, labels=types.index, autopct='%1.1f%%')
		plt.title('Subdomain types')
		plt.axis('equal')

		with BytesIO() as buff:
			plt.savefig(buff, format='png')
			plt.clf()
			buff.seek(0)
			figdata = base64.b64encode(buff.read())
			return figdata.decode('utf-8')

	API = 'https://sonar.omnisint.io/all/'

	try:
		data = requests.get(f'{API}{domain}')
		if data.status_code == 200:
			df = pd.DataFrame(json.loads(data.text))
			df.drop(columns=['subdomain', 'domain', 'tld'], inplace=True)
			results = {
				'graph': get_types_graph(df),
				'df_dict': df.to_dict(),
			}
		else:
			results = f'Error: {data.status_code} {data.reason}'
		status = data.status_code
	except:
		results = 'Este servicio no está disponible en este momento:'
		status = 503
	finally:
		return {'results': results, 'status': status}