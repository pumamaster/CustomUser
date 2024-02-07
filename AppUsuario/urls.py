from django.urls import path
from .views import LoginView, LogoutView, welcome

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', welcome, name='welcome'),

]