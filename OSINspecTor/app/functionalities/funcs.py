from app.functionalities.common.geo import get_geo
from app.functionalities.domain.emails import get_emails
from app.functionalities.domain.subdomains import get_subdomains
from app.functionalities.ip.reverse import get_reverse
from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest

class Functionality:

    def __init__(self, button_label: str, button_id: str, func):
        self.button_label = button_label
        self.button_id = button_id
        self.func = func

class FuncsConfig:
    
    funcs = {
        'sub': Functionality('Subdominios', 'btn_sub', get_subdomains), #F1
        'geo': Functionality('Geolocalizar', 'btn_geo', get_geo), #F2
        'dns': Functionality('DNS', 'btn_dns', None), #F3
        'mx': Functionality('MX', 'btn_mx', None), #F4
        'em': Functionality('Emails', 'btn_em', get_emails), #F5
        'rev': Functionality('Reverse', 'btn_rev', get_reverse), #F6
        'ran': Functionality('IP range', 'btn_ran', None), #F7
        'vul': Functionality('Vulns', 'btn_vul', None), #F8
    }

    domain_funcs = ('sub', 'geo', 'dns', 'mx', 'em', 'ran', 'vul')

    ip_funcs = ('geo', 'rev', 'vul')

    @staticmethod
    def get_buttons_info(t: tuple) -> tuple: # (ID, Label)
        funcs = FuncsConfig.funcs
        labels = []
        for option in t:
            labels.append((funcs[option].button_id, funcs[option].button_label))
        return labels

    @staticmethod
    def get_results(request: HttpRequest, t: tuple):
        dir = request.POST['dir']
        func = FuncsConfig.funcs[request.POST['method']].func
        if func is not None:
            try: 
                return JsonResponse({"results": func(dir)})
            except Exception as e:
                return JsonResponse({"results": f"Error: {e}"},status=418)