from django.contrib import admin
from .models import Venda, ItemVenda


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente','data_venda', 'valor_total')
    inlines = [ItemVendaInline]
    readonly_fields = ('valor_total',)

@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade', 'preco_unitario')