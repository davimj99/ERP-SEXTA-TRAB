from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from django.db import IntegrityError

# LISTAR CLIENTES
def clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': lista_clientes})


# CRIAR CLIENTE
def novos_clientes(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')

        try:
            Cliente.objects.create(
                nome=nome,
                email=email,
                telefone=telefone,
                cpf=cpf
            )
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('clientes')

        except IntegrityError:
            messages.error(request, f"CPF {cpf} já cadastrado.")
            return render(request, 'clientes/novos_clientes.html', {
                'nome': nome,
                'email': email,
                'telefone': telefone
            })

    return render(request, 'clientes/novos_clientes.html')


# EDITAR CLIENTE
def editar_clientes(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.nome = request.POST.get('nome')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.cpf = request.POST.get('cpf')

        try:
            cliente.save()
            messages.success(request, "Cliente atualizado!")
            return redirect('clientes')

        except IntegrityError:
            messages.error(request, "CPF já utilizado.")
            return render(request, 'clientes/editar_clientes.html', {'cliente': cliente})

    return render(request, 'clientes/editar_clientes.html', {'cliente': cliente})


def excluir_clientes(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()
        messages.success(request, "Cliente excluído!")
        return redirect('clientes')

    return redirect('clientes')