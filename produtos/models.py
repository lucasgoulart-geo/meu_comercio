from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizando_em = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # opcional

    def __str__(self):
        return self.nome