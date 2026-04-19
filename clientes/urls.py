from django.urls import path
from . import views

urlpatterns = [
    # Isso vai fazer a rota /clientes/ funcionar
    path('', views.clientes, name='clientes'), 
    path('novo/', views.novo_cliente, name='novo_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
] 
