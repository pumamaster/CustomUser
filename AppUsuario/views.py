from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')  # Redirige a la página de bienvenida
            else:
                error_message = "Nombre de usuario o contraseña incorrectos."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
        else:
            return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirige a la página de inicio de sesión
    
@login_required
def welcome(request):
    return render(request, 'welcome.html')