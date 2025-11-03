from django.shortcuts import render
from .models import Produto

def home(request):
    return render (request, 'index.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def contato(request):
    return render(request, 'contato.html')
# Create your views here.
