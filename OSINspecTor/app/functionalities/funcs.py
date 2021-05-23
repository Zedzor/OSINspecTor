from app.functionalities.common.geo import get_geo
from app.functionalities.domain.emails import get_emails
from app.functionalities.domain.subdomains import get_subdomains
from app.functionalities.ip.reverse import get_reverse
from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest

class Functionality:
    
    def __init__(self, button_label: str, button_id: str, post_option: str, func):
        self.button_label = button_label
        self.button_id = button_id
        self.post_option = post_option
        self.func = func

FUNCS = {
    1: Functionality('Subdominios', 'btn_sub', 'sub', get_subdomains), #Dominios
    2: Functionality('Geolocalizar', 'btn_geo', 'geo', get_geo), #Dominios e IP
    3: Functionality('DNS', 'btn_dns', None, None), #Dominios
    4: Functionality('MX', 'btn_mx', None, None), #Dominios
    5: Functionality('Emails', 'btn_em', 'em', get_emails), #Dominios
    6: Functionality('Reverse', 'btn_rev', 'rev', get_reverse), #IP
    7: Functionality('IP range', 'btn_ran', None, None), #Dominios
    8: Functionality('Vulns', 'btn_vul', None, None), #Dominios e IP
}

DOMAIN_FUNCS = (1,2,5)
#DOMAIN_FUNCS= (1,2,3,4,5,7,8)
IP_FUNCS = (2,6)
#IP_FUNCS = (6,8)


class Methods:

    @staticmethod
    def get_method(option: str, l: tuple):
        for i in l:
            if FUNCS[i].post_option == option:
                return FUNCS[i].func
        return None

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
    def get_ip_labels() -> tuple:
        return Buttons._get_labels(IP_FUNCS)


def form_post(request: HttpRequest, l: tuple):
    dir = request.POST['dir']
    func = Methods.get_method(request.POST['method'], l)
    if func is not None:
        try: 
            return JsonResponse({"results": func(dir)})
        except Exception as e:
            return JsonResponse({"results": f"Error: {e}"},status=418)