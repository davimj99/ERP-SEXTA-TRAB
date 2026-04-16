from django.urls import path
from .views import lista_vendas

urlpatterns = [
    path('', lista_vendas, name='vendas'),
]