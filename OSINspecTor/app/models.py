from django.db import models

# Create your models here.
from app.model.geo import get_geo
from app.model.domain.emails import get_emails
from app.model.domain.subdomains import get_subdomains
from app.model.ip.reverse import get_reverse

class Functionality:
    
    def __init__(self, button_label: str, button_id: str, func):
        self.button_label = button_label
        self.button_id = button_id
        self.func = func

FUNCS = {
    1: Functionality('Subdominios', 'btn_sub', get_subdomains), #Dominios
    2: Functionality('Geolocalizar', 'btn_geo', get_geo), #Dominios e IP
    3: Functionality('DNS', 'btn_dns', None), #Dominios
    4: Functionality('MX', 'btn_mx', None), #Dominios
    5: Functionality('Emails', 'btn_em', get_emails), #Dominios
    6: Functionality('Reverse', 'btn_rev', get_reverse), #IP
    7: Functionality('IP range', 'btn_ran', None), #Dominios
    8: Functionality('Vulns', 'btn_vul', None), #Dominios e IP
}

DOMAIN_FUNCS= (1,2,5)
#DOMAIN_FUNCS= (1,2,3,4,5,7,8)
IP_FUNCS = (2,6)
#IP_FUNCS = (6,8)


class Buttons:

    @staticmethod
    def _get_labels(l: tuple) -> tuple: # (ID, Label)
        labels = []
        for i in l:
            labels.append((FUNCS[i].button_id, FUNCS[i].button_label))
        return labels

    @staticmethod
    def get_domain_labels() -> tuple:
        return Buttons._get_labels(DOMAIN_FUNCS)

    @staticmethod
    def get_ip_labels():
        return Buttons._get_labels(IP_FUNCS)