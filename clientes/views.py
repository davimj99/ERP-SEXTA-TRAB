from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from django.db import IntegrityError

def clientes(request):
    # Puxa TODOS os clientes do banco de dados
    lista_de_clientes = Cliente.objects.all()
    
    # Envia essa lista para a página HTML usar
    return render(request, 'clientes.html', {'clientes': lista_de_clientes})

def novo_cliente(request):
    if request.method == "POST":
        # 1. Primeiro você cria as variáveis pegando do formulário
        nome_digitado = request.POST.get('nome')
        email_digitado = request.POST.get('email')
        telefone_digitado = request.POST.get('telefone')
        cpf_digitado = request.POST.get('cpf')

        try:
            # 2. Depois você usa essas variáveis para criar no banco
            Cliente.objects.create(
                nome=nome_digitado,
                email=email_digitado,
                telefone=telefone_digitado,
                cpf=cpf_digitado
            )
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('/clientes/')
        
        except IntegrityError:
            # 3. E aqui você usa as mesmas variáveis para devolver ao formulário
            messages.error(request, f"Erro: O CPF {cpf_digitado} já está cadastrado.")
            return render(request, 'novo_cliente.html', {
                'nome': nome_digitado, 
                'email': email_digitado, 
                'telefone': telefone_digitado
            })

    return render(request, 'novo_cliente.html')


# FUNÇÃO DE EDITAR
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        # Pegamos os dados do formulário
        novo_nome = request.POST.get('nome')
        novo_email = request.POST.get('email')
        novo_telefone = request.POST.get('telefone')
        novo_cpf = request.POST.get('cpf')

        try:
            # Tentamos salvar as alterações
            cliente.nome = novo_nome
            cliente.email = novo_email
            cliente.telefone = novo_telefone
            cliente.cpf = novo_cpf
            cliente.save()
            
            messages.success(request, "Cliente atualizado com sucesso!")
            return redirect('/clientes/')
            
        except IntegrityError:
            # Se o CPF já existir em outro cadastro, cai aqui:
            messages.error(request, f"Erro: O CPF {novo_cpf} já está em uso por outro cliente.")
            return render(request, 'editar_cliente.html', {'cliente': cliente})
    
    return render(request, 'editar_cliente.html', {'cliente': cliente})
# FUNÇÃO DE EXCLUIR
def excluir_cliente(request, id):
    # Busca o cliente e simplesmente apaga do banco
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('/clientes/')
