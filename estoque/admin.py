from django.contrib import admin
from .models import Estoque

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'atualizado_em', 'preco_total')
    search_fields = ('produto__nome',)