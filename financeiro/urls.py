from django.urls import path
from .views import lista_financeiro, lista_transacoes

urlpatterns = [
    path('', lista_financeiro, name='financeiro'),
    path('', lista_transacoes, name='lista_transacoes'),
]