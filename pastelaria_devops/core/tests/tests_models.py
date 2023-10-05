from django.test import TestCase
from pastelaria_devops.core.models import Produto
from pastelaria_devops.core.models import Venda
from pastelaria_devops.core.models import ProdutoVenda

# Create your tests here.
class TestModelProduto(TestCase):
    def setUp(self):
        # configura dados dos testes
        self.produto = Produto.objects.create(
            nome='Pastel de carne',
            preco=9.00
            )
        
    def test_preco_produto(self):
        self.assertEqual(self.produto.preco,9.00)

class TestModelVenda(TestCase):
    def setUp(self):
        self.pastel_de_carne = Produto.objects.create(nome='Pastel de carne', preco=9.00)
        self.pastel_de_queijo = Produto.objects.create(nome='Pastel de queijo', preco=9.00)
        self.venda1 = Venda.objects.create(
            data='2023-10-05',
        )
        self.produto_venda = ProdutoVenda.objects.create(
            venda=self.venda1,
            produto=self.pastel_de_queijo
            quantidade=10
        )

    #def test_soma_venda(self):



        