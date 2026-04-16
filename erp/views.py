from django.shortcuts import render
from produtos.models import Produto
from vendas.models import Venda
from estoque.models import Estoque

def dashboard(request):
    context = {
        'produtos': Produto.objects.all(),
        'vendas': Venda.objects.all(),
        'estoque': Estoque.objects.all(),
    }

    return render(request, 'dashboard.html', context)