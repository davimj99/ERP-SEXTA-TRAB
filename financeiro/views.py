from django.shortcuts import render
from .models import Transacao

def lista_transacoes(request):
    transacoes = Transacao.objects.all().order_by('-data')
    return render(request, 'lista.html', {'transacoes': transacoes})
def lista_financeiro(request):
    return render(request, 'lista.html')