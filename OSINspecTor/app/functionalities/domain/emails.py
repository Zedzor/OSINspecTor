from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re
from pandas import Series
from django.http import JsonResponse

def get_emails(domain): 
    sercode=True
    try:    
        def email_on_url(page, domain):
            soup = BeautifulSoup(page.text, 'html.parser')
            return re.findall(f"[A-Za-z0-9.]+@{domain}", soup.get_text())

        query=f"intext:\"@{domain}\""
        lista=[]
        for j in search(query,tld="com", num=20,stop=20,pause=2):
            if re.search("\.pdf$", j) is None:
                try:
                    page = requests.get(j)
                    lista+=email_on_url(page, domain)
                except:
                    pass
        if lista == []:
            sercode=False
            raise Exception("No se encontraron resultados para ese dominio")
        series = Series(lista).sort_values().drop_duplicates().reset_index(drop=True).to_dict()
        response = JsonResponse({'results':series})

    except Exception as e:
        if sercode:
            response = JsonResponse({'results':f'Este servicio no está disponible en este momento: {e}'}, status=429)
        else:
            response = JsonResponse({'results':f'{e}'}, status=404)
    finally:
        return response