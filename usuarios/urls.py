from django.urls import path
from .views import lista_usuarios,usuarios

urlpatterns = [
    path('', lista_usuarios, name='usuarios'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),

]