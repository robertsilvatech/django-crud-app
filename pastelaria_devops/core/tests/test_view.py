from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


class TestViewProdutosGeral(TestCase):
    def test_tabela_produtos_vazia(self):
        url = reverse('editar_produto', args=[1])
        response = self.client.get(url)
        self.assertNotEqual(response.status_code,200,"Existem produtos cadastrados na tabela produtos")

    def test_criar_novo_produto(self):
        url = reverse('novo_produto')
        data = {'nome': 'Pastel de teste', 'preco': 99.00}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302, f"Falha ao criar produto: {response.status_code}")