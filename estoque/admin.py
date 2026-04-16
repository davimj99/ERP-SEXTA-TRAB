from django.contrib import admin #importando o módulo de administração do Django.
from .models import Estoque

@admin.register(Estoque) #Esse é um decorator. Registrar o Estoque diretamente no admin
class EstoqueAdmin(admin.ModelAdmin): #classe de configuração do admin.
    list_display = ('produto', 'quantidade', 'atualizado_em', 'preco_total') #Define quais campos vão aparecer na lista de registros no admin.
    search_fields = ('produto__nome',) #Isso habilita a barra de busca no admin.S