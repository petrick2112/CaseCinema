import unittest
from unittest.mock import MagicMock, patch
from services.compra_service import CompraService

class TestCompraService(unittest.TestCase):
    @patch('services.compra_service.Compra')
    def test_criar_compra(self, MockCompra):
        # Arrange
        service = CompraService()
        cliente = "Cliente Teste"
        filme = "Filme Teste"
        qtd_ingressos = 2
        mock_compra_instance = MagicMock()
        MockCompra.return_value = mock_compra_instance

        # Act
        compra = service.criar_compra(cliente, filme, qtd_ingressos)

        # Assert
        MockCompra.assert_called_once_with(cliente, filme, qtd_ingressos)
        self.assertIn(mock_compra_instance, service.compras)
        self.assertEqual(compra, mock_compra_instance)

    def test_listar(self):
        service = CompraService()
        # Simulate compras
        compra1 = MagicMock()
        compra2 = MagicMock()
        service.compras.extend([compra1, compra2])

        compras_listadas = service.listar()
        self.assertEqual(compras_listadas, [compra1, compra2])

if __name__ == '__main__':
    unittest.main()