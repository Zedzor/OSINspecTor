from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re
from pandas import Series

def get_emails(domain):  
    try:    
        def email_on_url(page, domain):
            soup = BeautifulSoup(page.text, 'html.parser')
            return re.findall(f"[A-Za-z0-9.]+@{domain}", soup.get_text())

        query=f"intext:\"@{domain}\""
        lista=[]
        for j in search(query,tld="com", num=20,stop=20,pause=2):
            page = requests.get(j)
            lista+=email_on_url(page, domain)
    except Exception as e:
        print(f"El error fue {e}")
        raise e

    return Series(lista).sort_values().drop_duplicates().reset_index(drop=True).to_dict()