from django.urls import path
from .views import lista_estoque

urlpatterns = [
    path('', lista_estoque, name='estoque'),
]