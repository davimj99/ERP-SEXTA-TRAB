from django import forms #Importa o módulo de formulários do Django
from .models import Estoque #Importa o módulo de formulários do Django

class EstoqueForm(forms.ModelForm): #Aqui cria um formulário baseado em modelo (ModelForm).
    """
    Form → você cria tudo manual
    ModelForm → o Django cria os campos automaticamente baseado no model
    """
    class Meta:
        model = Estoque
        fields = [  #Define quais campos vão aparecer no formulário.
            'produto',
            'unidade_medida',
            'quantidade',
            'preco_unitario'
        ]