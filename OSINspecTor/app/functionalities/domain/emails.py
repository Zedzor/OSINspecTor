from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re
from pandas import Series

def get_emails(domain): 
    sercode=True; 
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
        return Series(lista).sort_values().drop_duplicates().reset_index(drop=True).to_dict()

    except Exception as e:
        if sercode:
            raise Exception(f"Este servicio no está disponible en este momento {e}")
        else:
            raise Exception(e)