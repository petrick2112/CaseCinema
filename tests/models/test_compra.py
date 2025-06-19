import unittest
from unittest.mock import Mock
from models.compra import Compra

class TestCompra(unittest.TestCase):
    def setUp(self):
        self.cliente = "Cliente Teste"
        self.filme = "Filme Teste"
        self.qtd_ingressos = 2
        self.compra = Compra(self.cliente, self.filme, self.qtd_ingressos)

    def test_compra_init(self):
        self.assertEqual(self.compra.cliente, self.cliente)
        self.assertEqual(self.compra.filme, self.filme)
        self.assertEqual(self.compra.qtd_ingressos, self.qtd_ingressos)
        self.assertIsInstance(self.compra.id, str)
        self.assertEqual(len(self.compra.id), 8)
        self.assertEqual(self.compra.produtos, [])

    def test_adicionar_produto(self):
        produto = Mock()
        produto.preco = 10.0
        self.compra.adicionar_produto(produto, 3)
        self.assertEqual(len(self.compra.produtos), 1)
        self.assertEqual(self.compra.produtos[0], (produto, 3))

    def test_total_sem_produtos(self):
        esperado = self.qtd_ingressos * 25.0
        self.assertEqual(self.compra.total(), esperado)

    def test_total_com_produtos(self):
        produto1 = Mock()
        produto1.preco = 10.0
        produto2 = Mock()
        produto2.preco = 5.0
        self.compra.adicionar_produto(produto1, 2)  # 2 * 10 = 20
        self.compra.adicionar_produto(produto2, 4)  # 4 * 5 = 20
        esperado = (self.qtd_ingressos * 25.0) + 20 + 20
        self.assertEqual(self.compra.total(), esperado)

if __name__ == "__main__":
    unittest.main()