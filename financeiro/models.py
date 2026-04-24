yfrom django.db import models

class Transacao(models.Model):

    TIPOS = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('crédito', 'Débito'),
    )

    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao