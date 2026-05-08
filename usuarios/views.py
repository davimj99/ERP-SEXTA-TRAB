from django.shortcuts import render
from .models import Usuario

#def lista_usuarios(request):
    #return render(request, 'usuario/lista.html')

def lista_usuarios(request):
    usuario = Usuario.objects.all().order_by('-criado_em')
    return render(request, 'lista.html', {'usuarios': usuarios})