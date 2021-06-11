from OSINspecTor.users.forms import LoginForm, SignupFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.
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

def index(request):
    loginError=""

    if 'username' in request.POST:
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            loginError="Error de login"

    loginForm = LoginForm()
    signupForm = SignupFrom()

    if request.user.is_authenticated:
        context={'user':request.user, 'login_form':loginForm,'signup_form':signupForm,'loginError':loginError}
    else:
        context={'login_form':loginForm,'signup_form':signupForm,'loginError':loginError}
    
    return render(request, 'user/index-html', context)