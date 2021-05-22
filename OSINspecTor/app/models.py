from django.db import models

# Create your models here.
from app.model.geo import get_geo
from app.model.domain.emails import get_emails
from app.model.domain.subdomains import get_subdomains
from app.model.ip.reverse import get_reverse


class Buttons:
    LABELS = {
        1: ('btn_sub', 'Subdominios'), #Dominios
        2: ('btn_geo', 'Geolocalizar'), #Dominios e IP
        3: ('btn_dns', 'DNS'), #Dominios
        4: ('btn_mx', 'MX'), #Dominios
        5: ('btn_em', 'Emails'), #Dominios
        6: ('btn_rev', 'Reverse'), #IP
        7: ('btn_ran', 'IP range'), #Dominios
        8: ('btn_vul', 'Vulns'), #Dominios e IP
    }

    @staticmethod
    def _get_labels(l: tuple):
        labels = []
        for i in l:
            labels.append((Buttons.LABELS[i][0], Buttons.LABELS[i][1]))
        return labels

    @staticmethod
    def get_domain_labels():
        return Buttons._get_labels((1,2,5))

    @staticmethod
    def get_ip_labels():
        return Buttons._get_labels((2,6))