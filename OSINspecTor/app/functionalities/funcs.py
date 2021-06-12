from app.functionalities.common.geo import get_geo
from app.functionalities.common.vuln import get_vulns
from app.functionalities.domain.emails import get_emails
from app.functionalities.domain.subdomains import get_subdomains
from app.functionalities.ip.reverse import get_reverse
from django.http import JsonResponse

class Functionality:

    def __init__(self, button_label: str, button_id: str, func):
        self.button_label = button_label
        self.button_id = button_id
        self.func = func

class FuncsConfig:
    
    FUNCS = {
        'sub': Functionality('Subdominios', 'btn_sub', get_subdomains), #F1
        'geo': Functionality('Geolocalizar', 'btn_geo', get_geo), #F2
        'dns': Functionality('DNS', 'btn_dns', None), #F3
        'mx': Functionality('MX', 'btn_mx', None), #F4
        'em': Functionality('Emails', 'btn_em', get_emails), #F5
        'rev': Functionality('Reverse', 'btn_rev', get_reverse), #F6
        'ran': Functionality('IP range', 'btn_ran', None), #F7
        'vul': Functionality('Vulns', 'btn_vul', get_vulns), #F8
    }

    DOMAIN_FUNCS = ('sub', 'geo', 'dns', 'mx', 'em', 'ran', 'vul')

    IP_FUNCS = ('geo', 'rev', 'vul')

    DOMAIN_MODE = 'DOMAIN'

    IP_MODE = 'IP'

    @classmethod
    def _get_buttons_info(cls, options: tuple) -> list[tuple[str, str]]:
        labels = []
        for option in options:
            info = cls.FUNCS[option]
            labels.append((info.button_id, info.button_label))
        return labels

    @classmethod
    def get_domain_buttons(cls) -> list[tuple[str, str]]:
        return cls._get_buttons_info(cls.DOMAIN_FUNCS)

    @classmethod
    def get_ip_buttons(cls) -> list[tuple[str, str]]:
        return cls._get_buttons_info(cls.IP_FUNCS)


    @classmethod
    def get_results(cls, option: str, dir: str, mode: str) -> JsonResponse:
        try:
            if mode == cls.DOMAIN_MODE:
                if option not in cls.DOMAIN_FUNCS:
                    raise Exception('Funcionalidad de dominio no válida.')
                else:
                    pass # Comprobar dominio

            if mode == cls.IP_MODE:
                if option not in cls.IP_FUNCS:
                    raise Exception('Funcionalidad de IP no válida.')
                else:
                    pass # Comprobar IP

        except Exception as e:
            results = JsonResponse({'results': f'Error: {e}'}, status=400)
        else:
            try:
                func = cls.FUNCS[option].func
                if func is None:
                    raise Exception('Funcionalidad no implementada todavía.')
            except Exception as e:
                results = JsonResponse({'results': f'Error: {e}'}, status=501)
            else:
                results = func(dir)
        finally:
            return results