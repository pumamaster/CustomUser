from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm

class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm
    success_url=reverse_lazy('welcome')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView,self).dispatch(request, *args,**kwargs)
        
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            
            form.add_error(None, "Invalid username or password.")
            return self.form_invalid(form)

'''class LoginView(View):
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
            return render(request, 'login.html', {'form': form})'''

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirige a la página de inicio de sesión
    
@login_required
def welcome(request):
    return render(request, 'welcome.html')