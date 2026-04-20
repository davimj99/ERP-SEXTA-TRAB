from django.db import models #Impota tabelas do banco, campos ,relacionamentos
from produtos.models import Produto #Importa realacionamento produto e estoque (estoque depende de um produto.)
from decimal import Decimal #Importa a classe Decimal. Evita erros de cálculo com float, precisão 

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE) #Relacionamento com Produto (chave estrangeira).
    #cada estoque pertence a um produto , on_delete=models.CASCADE:se o produto for deletado o estoque também é deletado

    UNIDADES = [ #ista de opções para unidade de medida.
    ('UN', 'Unidade'),
    ('KG', 'Quilograma'),
    ('L', 'Litro'),
    ('M', 'Metro'),
    ]

    unidade_medida = models.CharField(max_length=5, choices=UNIDADES) #Campo de texto com opções limitadas.
    quantidade = models.DecimalField(max_digits=10, decimal_places=2) #Campo numérico com casas decimais.

    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0) #Preço por unidade do produto. default=0 evita erros se não prencher.
    preco_total = models.DecimalField(max_digits=12, decimal_places=2, default=0) #Campo para armazenar o valor total.

    atualizado_em = models.DateTimeField(auto_now=True) #Data automática de atualização.

    data_validade = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs): #Antes de salvar no banco:calcula o preço total //
        self.preco_total = Decimal(self.quantidade) * Decimal(self.preco_unitario)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} {self.unidade_medida}"
