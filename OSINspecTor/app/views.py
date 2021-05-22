from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Buttons
from app.model.geo import get_geo
from app.model.ip.reverse import get_reverse
from app.model.domain.subdomains import get_subdomains

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

def ip(request: HttpRequest):

    contex = {
        'cabecera': "Búsqueda por IP",
        'form_label': 'Introduzca una IP:',
        'buttons': Buttons.get_ip_labels(),
    }
    return render(request, 'busqueda.html', contex)

def rev(request):
    if request.method == 'POST':
        ip = request.POST['ip']
        resolucion = get_reverse(ip)
        return resolucion
    else:
        return HttpResponse("Peticion no valida")

def geo(request):
    if request.method == 'POST':
        ip = request.POST['ip']
        localizacion = get_geo(ip)
        return localizacion
    else:
        return HttpResponse("Peticion no valida")

def sub(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        subdominios = get_subdomains(domain)
        return subdominios
    else:
        return HttpResponse("Peticion no valida")
    