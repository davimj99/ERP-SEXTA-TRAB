from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Estoque

# O SEGREDO ESTÁ AQUI: Precisamos importar o Produto do outro app!
from produtos.models import Produto 

# 1. FUNÇÃO DE LISTAR (A Tabela)
def estoque(request):
    lista_estoque = Estoque.objects.all()
    return render(request, 'estoque/estoque.html', {'estoque': lista_estoque})

# 2. FUNÇÃO DE REGISTRAR NOVO ESTOQUE
def novo_estoque(request):
    # Buscamos todos os produtos para mandar para a caixa de seleção do HTML
    produtos_cadastrados = Produto.objects.all()

    if request.method == "POST":
        produto_id = request.POST.get('produto_id')
        unidade = request.POST.get('unidade_medida')
        qtd = request.POST.get('quantidade')
        preco_uni = request.POST.get('preco_unitario')
        validade = request.POST.get('data_validade')
        
        try:
            # Primeiro, achamos o Produto real no banco de dados
            produto_selecionado = Produto.objects.get(id=produto_id)
            
            # Depois, criamos o estoque ligado a esse produto
            Estoque.objects.create(
                produto=produto_selecionado,
                unidade_medida=unidade,
                quantidade=qtd,
                preco_unitario=preco_uni,
                data_validade=validade,
            )
            messages.success(request, "Estoque registrado com sucesso!")
            return redirect('/estoque/')
            
        except Exception as e:
            messages.error(request, f"Erro ao registrar: {e}")

    # Enviamos a lista de produtos para a tela renderizar as opções
    return render(request, 'estoque/novo_estoque.html', {'produtos': produtos_cadastrados})
