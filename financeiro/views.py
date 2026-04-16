from django.shortcuts import render

def lista_financeiro(request):
    return render(request, 'financeiro/lista.html')