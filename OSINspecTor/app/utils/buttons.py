from app.model.geo import get_geo
from app.model.domain.emails import get_emails
from app.model.domain.subdomains import get_subdomains
from app.model.ip.reverse import get_reverse


class Buttons:
    FUNCS = {
        1: ('btn_sub', 'Subdominios', get_subdomains), #Dominios
        2: ('btn_geo', 'Geolocalizar', get_geo), #Dominios e IP
        3: ('btn_dns', 'DNS', None), #Dominios
        4: ('btn_mx', 'MX', None), #Dominios
        5: ('btn_em', 'Emails', get_emails), #Dominios
        6: ('btn_rev', 'Reverse', get_reverse), #IP
        7: ('btn_ran', 'IP range', None), #Dominios
        8: ('btn_vul', 'Vulns', None), #Dominios e IP
    }

    DOMAIN_FUNCS = (1, 2, 3, 4, 5, 6, 8)
    IP_FUNCS = (2, 6, 8)

    def _get_funcs(self, l: tuple):
        funcs = []
        for i in l:
            funcs.append((self.FUNCS[i][0], self.FUNCS[i][1]))
        return funcs

    def get_domain_funcs(self):
        return self._get_funcs((1,2,5))

    def get_ip_funcs(self):
        return self._get_funcs((2,6))