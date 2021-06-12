from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.functionalities.funcs import FuncsConfig

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html')


def _dominio_e_ip(request: HttpRequest, context: dict, mode: str):
    if request.method == 'GET':
        return render(request, 'busqueda.html', context)
    elif request.method == 'POST':
        try:
            option = request.POST['method']
            dir = request.POST['dir']
        except Exception as e:
            return JsonResponse({'results': f'Error: {e}'}, status=400)
        else:
            return FuncsConfig.get_results(option, dir, mode)
    else:
        return JsonResponse({'results': 'Método no permitido.'}, status=405)

@csrf_exempt
def dominio(request: HttpRequest):
    context = {
        'cabecera': 'Búsqueda por dominio',
        'form_label': 'Introduzca un dominio:',
        'buttons': FuncsConfig.get_domain_buttons(),
    }
    return _dominio_e_ip(request, context, FuncsConfig.DOMAIN_MODE)

@csrf_exempt
def ip(request: HttpRequest):
    context = {
        'cabecera': 'Búsqueda por IP',
        'form_label': 'Introduzca una IP:',
        'buttons': FuncsConfig.get_ip_buttons(),
    }
    return _dominio_e_ip(request, context, FuncsConfig.IP_MODE)
