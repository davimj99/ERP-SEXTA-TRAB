from django.urls import path
from . import views

urlpatterns = [
    # Isso vai fazer a rota /clients/ funcionar
    path('', views.clients, name='clients'), 
    path('new/', views.new_clients, name='new_clients'),
    path('edit/<int:id>/', views.edit_clients, name='edit_clients'),
    path('excluir/<int:id>/', views.excluir_clients, name='excluir_clients'),
]
