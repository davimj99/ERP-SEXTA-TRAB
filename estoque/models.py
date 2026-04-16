from django.db import models
from produtos.models import Produto

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    UNIDADES = [
    ('UN', 'Unidade'),
    ('KG', 'Quilograma'),
    ('L', 'Litro'),
    ('M', 'Metro'),
    ]

    unidade_medida = models.CharField(max_length=5, choices=UNIDADES)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preco_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    atualizado_em = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.preco_total = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} {self.unidade_medida}"