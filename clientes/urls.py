from django.urls import path
from . import views

urlpatterns = [
    # Isso vai fazer a rota /clientes/ funcionar
    path('', views.clientes, name='clientes'), 
    path('novo/', views.novos_clientes, name='novos_clientes'),
    path('edit/<int:id>/', views.editar_clientes, name='editar_clientes'),
    path('excluir/<int:id>/', views.excluir_clientes, name='excluir_clientes'),
]
