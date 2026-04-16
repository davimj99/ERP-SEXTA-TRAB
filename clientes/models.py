from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome
    
