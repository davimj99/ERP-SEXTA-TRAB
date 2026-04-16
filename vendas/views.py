from django.shortcuts import render

def lista_vendas(request):
    return render(request, 'vendas/lista.html')