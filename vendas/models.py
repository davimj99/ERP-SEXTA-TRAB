from django.db import models
from produtos.models import Produto


class Venda(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda {self.id}"

    def calcular_total(self):
        total = sum(item.subtotal() for item in self.itens.all())
        self.valor_total = total
        self.save()

    def baixar_estoque(self):
        for item in self.itens.all():
            produto = item.produto
            produto.estoque -= item.quantidade
            produto.save()


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.venda.calcular_total()