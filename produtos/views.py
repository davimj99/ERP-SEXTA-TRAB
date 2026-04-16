from django.shortcuts import render #junta um template HTML + dados + request e devolve para uma página pronta

def lista_produtos(request): #representa a requisição do usuário (quando alguém acessa a página)
    return render(request, 'produtos/lista.html') 

"""
request → a requisição do usuário
o arquivo HTML que será exibido
Views são o **cérebro do sistema**.
"""