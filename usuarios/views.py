from django.shortcuts import render
from .models import Usuario

def lista_usuarios(request):
    return render(request, 'usuarios/lista.html')
    from django.shortcuts import render


def lista_usuarios(request):
    usuarios = Usuario.objects.all().order_by('-criado_em')
    return render(request, 'lista.html', {'usuarios': usuarios})