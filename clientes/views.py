from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente # Importa o banco de dados que você criou
from django.db import IntegrityError

def clients(request): # Nome da função
    # Use o nome do Modelo (Cliente) para buscar no banco
    lista_clientes = Cliente.objects.all() 
    
    return render(request, 'clients.html', {'clientes': lista_clientes})

# ADICIONE ESTA NOVA FUNÇÃO:
def new_clients(request):
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
            return redirect('/clients/')
        
        except IntegrityError:
            # 3. E aqui você usa as mesmas variáveis para devolver ao formulário
            messages.error(request, f"Erro: O CPF {cpf_digitado} já está cadastrado.")
            return render(request, 'new_clients.html', {
                'nome': nome_digitado, 
                'email': email_digitado, 
                'telefone': telefone_digitado
            })

    return render(request, 'new_clients.html')

# FUNÇÃO DE EDITAR
def edit_clients(request, id):
    # MUDE AQUI: Use 'Cliente' (Maiúsculo) para buscar no banco
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        new_nome = request.POST.get('nome')
        new_email = request.POST.get('email')
        new_telefone = request.POST.get('telefone')
        new_cpf = request.POST.get('cpf')

        try:
            # Salvando as alterações na variável no singular
            cliente.nome = new_nome
            cliente.email = new_email
            cliente.telefone = new_telefone
            cliente.cpf = new_cpf
            cliente.save()
            
            messages.success(request, "Cliente atualizado com sucesso!")
            return redirect('/clients/')
            
        except IntegrityError:
            messages.error(request, f"Não foi possível salvar: O CPF {new_cpf} já pertence a outro cliente.")
            return render(request, 'edit_clients.html', {'cliente': cliente})
        
    return render(request, 'edit_clients.html', {'cliente': cliente})

# FUNÇÃO DE EXCLUIR
def excluir_clients(request, id):
    # MUDE AQUI TAMBÉM: Use 'Cliente' com C maiúsculo
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('/clients/')
