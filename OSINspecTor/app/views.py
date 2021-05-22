from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from app.utils.buttons import Buttons

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html')

def dominio(request: HttpRequest):

    contex = {
        'cabecera': "Búsqueda por dominio",
        'form_label': 'Introduzca un dominio:',
        'buttons': Buttons().get_domain_funcs(),
    }
    return render(request, 'busqueda.html', contex)

def ip(request: HttpRequest):

    contex = {
        'cabecera': "Búsqueda por IP",
        'form_label': 'Introduzca una IP:',
        'buttons': Buttons().get_ip_funcs(),
    }
    return render(request, 'busqueda.html', contex)