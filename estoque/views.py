from django.shortcuts import render

def lista_estoque(request):
    return render(request, 'estoque/lista.html')
