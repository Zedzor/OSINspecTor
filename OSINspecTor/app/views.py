from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.functionalities.funcs import Buttons, Methods, DOMAIN_FUNCS, IP_FUNCS

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html')

def dominio(request: HttpRequest):

    contex = {
        'cabecera': "Búsqueda por dominio",
        'form_label': 'Introduzca un dominio:',
        'buttons': Buttons.get_domain_labels(),
    }
    return render(request, 'busqueda.html', contex)

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
        ip = request.POST['dir']
        func = Methods.get_method(request.POST['method'], IP_FUNCS)
        if func is not None:
            return JsonResponse({"results": func(ip)})
    
    return HttpResponse("Peticion no valida")
