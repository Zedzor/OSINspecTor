from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.functionalities.funcs import FuncsConfig
from app.forms import LoginForm, SignupFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html')


def _dominio_e_ip(request: HttpRequest, context: dict, mode: str):
    if request.method == 'GET':
        return render(request, 'busqueda.html', context)
    elif request.method == 'POST':
        try:
            option = request.POST['method']
            dir = request.POST['dir'].strip()
            if dir.startswith('www'):
                dir = dir.replace('www', '')
        except Exception as e:
            return JsonResponse({'results': f'Error: {e}'}, status=400)
        else:
            data = FuncsConfig.get_results(option, dir, mode)
            results = data['results']
            status = data['status']
            return JsonResponse({'results': results}, status=status)
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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=contraseña)
            login(request, user)
            return redirect('index')
        return render(request, 'users/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(request.GET['next'])
