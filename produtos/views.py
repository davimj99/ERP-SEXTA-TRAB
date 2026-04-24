from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto
from django.db import IntegrityError

def produtos(request):
    lista_produtos = Produto.objects.all() 
    return render(request, 'produtos/produto.html', {'produtos': lista_produtos})

def novo_produto(request):
    if request.method == "POST":
        nome_digitado = request.POST.get('nome')
        descricao_digitada = request.POST.get('descricao')
        preco_digitado = request.POST.get('preco')
        
        try: 
            Produto.objects.create(
                nome=nome_digitado,
                descricao=descricao_digitada,
                preco=preco_digitado
            )
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect('produtos')
            
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar produto: {e}")
            return render(request, 'novo_produto.html', {
                'nome': nome_digitado,
                'descricao': descricao_digitada,
                'preco': preco_digitado
            })

    return render(request, 'produtos/novo_produto.html')

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        
        try:
            produto.save()
            messages.success(request, f"Produto '{produto.nome}' atualizado com sucesso!")
            return redirect('produtos')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar: {e}")

    return render(request, 'produtos/editar_produto.html', {'produto': produto})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    nome_produto = produto.nome
    produto.delete()
    messages.success(request, f"Produto '{nome_produto}' removido com sucesso!")
    return redirect('produtos')
