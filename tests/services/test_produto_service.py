import unittest
from services.produto_service import ProdutoService
from models.produto import Produto

class TestProdutoService(unittest.TestCase):
    def setUp(self):
        self.service = ProdutoService()

    def test_listar_returns_all_produtos(self):
        produtos = self.service.listar()
        self.assertEqual(len(produtos), 3)
        self.assertIsInstance(produtos[0], Produto)
        self.assertEqual(produtos[0].nome, "Pipoca")
        self.assertEqual(produtos[0].preco, 10.0)
        self.assertEqual(produtos[1].nome, "Chocolate")
        self.assertEqual(produtos[1].preco, 7.0)
        self.assertEqual(produtos[2].nome, "Refrigerante")
        self.assertEqual(produtos[2].preco, 6.0)

if __name__ == "__main__":
    unittest.main()