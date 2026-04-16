from django.shortcuts import render, redirect
from .models import Estoque
from .forms import EstoqueForm

def lista_estoque(request):
    estoque = Estoque.objects.all()
    return render(request, 'estoque/estoque.html', {'estoque': estoque})

def criar_estoque(request):
    form = EstoqueForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'estoque/criar_estoque.html', {
        'form': form
    })
def save(self, *args, **kwargs):
    self.preco_total = self.quantidade * self.preco_unitario
    super().save(*args, **kwargs)