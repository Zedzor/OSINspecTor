from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re

def email_on_url(page, domain):
        soup = BeautifulSoup(page.text, 'html.parser')
        return re.findall(f"[A-Za-z0-9.]+@{domain}", soup.get_text())


def emails(domain):
    query=f"intext:\"@{domain}\""
    lista=[]
    for j in search(query,tld="com", num=20,stop=20,pause=1.5):
        page = requests.get(j)
        lista+=email_on_url(page, domain)
    return set(lista)