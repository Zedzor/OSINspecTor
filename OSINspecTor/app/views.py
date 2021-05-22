from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from app.utils.buttons import Buttons

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html')

def dominio(request: HttpRequest):
    buttons = []
    for i in [1,2,5]: # Cambiar por Buttons.domain_funcs
        buttons.append(Buttons.funcs[i])

    contex = {
        'cabecera': "Búsqueda por dominio",
        'form_label': 'Introduzca un dominio:',
        'buttons': buttons,
    }
    return render(request, 'busqueda.html', contex)

def ip(request: HttpRequest):
    buttons = []
    for i in [2]: # Cambiar por Buttons.ip_funcs
        buttons.append(Buttons.funcs[i])

    contex = {
        'cabecera': "Búsqueda por IP",
        'form_label': 'Introduzca una IP:',
        'buttons': buttons,
    }
    return render(request, 'busqueda.html', contex)