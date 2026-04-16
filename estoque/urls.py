from django.urls import path # A função path, que é usada para criar rotas URLs no Django.
from .views import lista_estoque, criar_estoque #Importa as funções da sua views.py, receber a requisição do usuário/processa dados/retornar uma página HTML

urlpatterns = [ #Lista onde você define todas as rotas desse app.
    path('', lista_estoque, name='estoque'), #'' → URL vazia (ex: /estoque/), lista_estoque : função executada / name='estoque' : nome interno da rota
    path('criar/', criar_estoque, name='criar_estoque'), #'criar/'  URL: /estoque/criar/ ; criar_estoque : função chamada / nome da rota =  name='criar_estoque' 
]

#http://127.0.0.1:8000/estoque/  ou localhost:8000/estoque
#http://127.0.0.1:8000/estoque/criar/