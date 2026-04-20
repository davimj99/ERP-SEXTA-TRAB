from django.urls import path
from .views import produtos, novo_produto, editar_produto, excluir_produto

urlpatterns = [
    path('', produtos, name='produtos'),
    
    path('novo/', novo_produto, name='novo_produto'),
    path('edit/<int:id>/', editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', excluir_produto, name='excluir_produto'),
]
