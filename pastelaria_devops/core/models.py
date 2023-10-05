from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField(verbose_name='Preço', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    criado = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    itens = models.ManyToManyField('Produto', through='ProdutoVenda')

    def __str__(self):
        return f'{self.id} - Venda em {self.criado}'
    
class ProdutoVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.quantidade} de {self.produto}'