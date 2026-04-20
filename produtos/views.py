from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto # Importando o seu modelo bonitão
from django.db import IntegrityError

# 1. FUNÇÃO DE LISTAR (A Tabela)
def produtos(request):
    # Busca todos os produtos no banco de dados
    lista_produtos = Produto.objects.all() 
    return render(request, 'produtos.html', {'produtos': lista_produtos})

# 2. FUNÇÃO DE CRIAR NOVO
def novo_produto(request):
    if request.method == "POST":
        # Pegando apenas os 3 campos necessários do formulário
        nome_digitado = request.POST.get('nome')
        descricao_digitada = request.POST.get('descricao')
        preco_digitado = request.POST.get('preco')
        
        try:
            # Salvando no banco. 
            # (O SKU será gerado sozinho pela sua função save() do models.py!)
            Produto.objects.create(
                nome=nome_digitado,
                descricao=descricao_digitada,
                preco=preco_digitado
            )
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect('/produtos/')
            
        except Exception as e:
            # Caso dê algum erro (ex: preço com letra em vez de número)
            messages.error(request, f"Erro ao cadastrar produto: {e}")
            return render(request, 'novo_produto.html', {
                'nome': nome_digitado,
                'descricao': descricao_digitada,
                'preco': preco_digitado
            })

    return render(request, 'novo_produto.html')

def editar_produto(request, id):
    # Buscamos o produto específico pelo ID
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        # Pegamos os novos dados do formulário
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        
        try:
            produto.save()
            messages.success(request, f"Produto '{produto.nome}' atualizado com sucesso!")
            return redirect('/produtos/')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar: {e}")

    # Se for GET, apenas mostra a página com os dados atuais do produto
    return render(request, 'editar_produto.html', {'produto': produto})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    nome_produto = produto.nome
    produto.delete()
    messages.success(request, f"Produto '{nome_produto}' removido com sucesso!")
    return redirect('/produtos/')
