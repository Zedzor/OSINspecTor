from app.model.geo import get_geo
from app.model.domain.emails import get_emails
from app.model.domain.subdomains import get_subdomains
from app.model.ip.reverse import get_reverse


class Buttons:
    funcs = {
        1: ('Subdominios', get_subdomains), #Dominios
        2: ('Geolocalizar', get_geo), #Dominios e IP
        3: ('DNS', None), #Dominios
        4: ('MX', None), #Dominios
        5: ('Emails', get_emails), #Dominios
        6: ('Reverse', get_reverse), #IP
        7: ('IP range', None), #Dominios
        8: ('Vulns', None), #Dominios e IP
    }

    domain_funcs = (1, 2, 3, 4, 5, 6, 8)

    ip_funcs = (2, 6, 8)