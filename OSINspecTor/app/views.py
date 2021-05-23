from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.functionalities.funcs import Buttons, Methods, DOMAIN_FUNCS, IP_FUNCS, form_post

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html')

@csrf_exempt
def dominio(request: HttpRequest):
    if request.method == 'GET':    
        contex = {
            'cabecera': "Búsqueda por dominio",
            'form_label': 'Introduzca un dominio:',
            'buttons': Buttons.get_domain_labels(),
        }
        return render(request, 'busqueda.html', contex)

    if request.method == 'POST':
        return form_post(request, DOMAIN_FUNCS)

    return HttpResponse("Peticion no valida")


@csrf_exempt
def ip(request: HttpRequest):
    if request.method == 'GET':
        contex = {
            'cabecera': "Búsqueda por IP",
            'form_label': 'Introduzca una IP:',
            'buttons': Buttons.get_ip_labels(),
        }
        return render(request, 'busqueda.html', contex)

    if request.method == 'POST':
        return form_post(request, IP_FUNCS)

    return HttpResponse("Peticion no valida")
