from django.urls import path
from .views import estoque, novo_estoque

urlpatterns = [
    # A rota principal que abre a lista de estoque
    path('', estoque, name='estoque'),
    
    # A rota que abre o formulário para registrar nova entrada
    path('new/', novo_estoque, name='novo_estoque'), #'criar/'  URL: /estoque/criar/ ; criar_estoque : função chamada / nome da rota =  name='criar_estoque' 
]

#http://127.0.0.1:8000/estoque/  ou localhost:8000/estoque
#http://127.0.0.1:8000/estoque/criar/
