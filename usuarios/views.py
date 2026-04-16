from django.shortcuts import render

def lista_usuarios(request):
    return render(request, 'usuarios/lista.html')