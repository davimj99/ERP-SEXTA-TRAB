from django.db import models

class Cliente(models.Model):
    # Campos do Banco de Dados
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    email = models.EmailField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    
    # Controle de Status (Ativo/Inativo que temos na tabela)
    ativo = models.BooleanField(default=True, verbose_name="Cliente Ativo?")
    
    # Data automática de quando o cliente foi cadastrado
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # Isso faz com que o nome do cliente apareça bonitinho no painel do Django
    def __str__(self):
        return self.nomes
