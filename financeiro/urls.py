from django.urls import path
from .views import lista_financeiro

urlpatterns = [
    path('', lista_financeiro, name='financeiro'),
]