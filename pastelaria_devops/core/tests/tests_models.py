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



        