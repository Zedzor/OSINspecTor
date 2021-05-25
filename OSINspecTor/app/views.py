from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.functionalities.funcs import FuncsConfig

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html')


def _dominio_e_ip(request: HttpRequest, context: dict, funcs: tuple):
    if request.method == 'GET':
        return render(request, 'busqueda.html', context)

    if request.method == 'POST':
        return FuncsConfig.get_results(request, funcs)

    return JsonResponse({"results":"Petición no valida."}, status=405)

@csrf_exempt
def dominio(request: HttpRequest):
    FUNCS = FuncsConfig.domain_funcs
    context = {
        'cabecera': "Búsqueda por dominio",
        'form_label': 'Introduzca un dominio:',
        'buttons': FuncsConfig.get_buttons_info(FUNCS),
    }
    return _dominio_e_ip(request, context, FUNCS)

@csrf_exempt
def ip(request: HttpRequest):
    FUNCS = FuncsConfig.ip_funcs
    context = {
        'cabecera': "Búsqueda por IP",
        'form_label': 'Introduzca una IP:',
        'buttons': FuncsConfig.get_buttons_info(FUNCS),
    }
    return _dominio_e_ip(request, context, FUNCS)
