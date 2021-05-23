import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def get_subdomains(dominio: str) -> dict:

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

	suburl = "https://sonar.omnisint.io/all/"+dominio
	data = requests.get(suburl)
	df = pd.DataFrame(json.loads(data.text))
	df.drop(columns=['subdomain', 'domain', 'tld'], inplace=True)
	data = {
		'graph': get_types_graph(df),
		'df_dict': df.to_dict(),
	}
	return data