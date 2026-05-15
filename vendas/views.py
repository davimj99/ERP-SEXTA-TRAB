from django.shortcuts import render
from .models import Venda

def lista_vendas(request):

    vendas = Venda.objects.prefetch_related(
        'itens__produto'
    ).all().order_by('-data_venda')

    return render(request, 'vendas.html', {
        'vendas': vendas
    })