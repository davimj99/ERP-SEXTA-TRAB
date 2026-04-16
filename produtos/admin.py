from django.contrib import admin #Importa o sistema de admin do Django
from .models import Produto #importando o model para o admin pra registrar la

@admin.register(Produto) #decorator que vai registrar o model produto no admin
class ProdutoAdmin(admin.ModelAdmin): #classe de personaliza de produto pra aparecer no admin, admin.ModelAdmin classe padrão do Django para configuração
    list_display = ('nome',  'preco', 'ativo') #list_display Define quais colunas aparecem na lista do admin
    search_fields = ('nome',) #search_fields Adiciona uma barra de busca
    list_filter = ('ativo',) #list_filter Adiciona um filtro lateral no admin
#TODAS FUNÇÃO LEMBRAM SIDEBAR E UM NAV

#Serve para gerenciar dados do sistema (tipo um mini ERP interno)