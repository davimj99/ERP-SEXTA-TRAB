import uuid
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True, blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nome} - {self.sku}"

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)