import uuid #módulo `uuid`, que serve para gerar identificadores únicos universais. (sku automático)
from django.db import models

#Classe do produto
class Produto(models.Model): #Criamos uma classe produto e o models.Model diz pro db que isso é uma tabela
    nome = models.CharField(max_length=150) #Campo de texto curto (VARCHAR no banco) e limita 150 caracteres
    descricao = models.TextField() #Text igual um vachar sem limite fixo
    preco = models.DecimalField(max_digits=10, decimal_places=2)#Campo para valores monetários , max_digits=10 total de digitos , decimal_places=2 casas decimais
    sku = models.CharField(max_length=50, unique=True, blank=True) #Codigo do produto, unique=True pra não repetir o cod, blank=True pode ser vazio no forms
    ativo = models.BooleanField(default=True) #Campo verdadeiro ou falso, default=True : quando cria, já vem ativo automaticamente

#Representação do objeto
    def __str__(self): #Esse método define como o produto vai aparecer no Django Admin e em prints
        return f"{self.nome} - {self.sku}"

    def save(self, *args, **kwargs): #**sobrescrevendo o método save()** do Django., permite executar lógica antes de salvar no banco.
        if not self.sku:
            self.sku = str(uuid.uuid4())[:8].upper() #- `uuid.uuid4()` → gera um código único tipo:, [:8] pega só os 8 primeiros caracteres, .upper tudo em maiusculo
        super().save(*args, **kwargs) #Aqui chama o método original do Django para realmente salvar o produto no banco de dados.