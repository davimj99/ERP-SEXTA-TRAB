from django.urls import path
from .views import lista_estoque, criar_estoque

urlpatterns = [
    path('', lista_estoque, name='estoque'),
    path('criar/', criar_estoque, name='criar_estoque'),
]