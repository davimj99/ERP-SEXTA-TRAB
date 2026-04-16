from django import forms
from .models import Estoque

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = [
            'produto',
            'unidade_medida',
            'quantidade',
            'preco_unitario'
        ]