import unittest
from unittest.mock import MagicMock, patch
from services.reserva_service import ReservaService

class TestReservaService(unittest.TestCase):
    def setUp(self):
        # Patch Reserva to avoid dependency on models.reserva.Reserva implementation
        patcher = patch('services.reserva_service.Reserva')
        self.mock_reserva_class = patcher.start()
        self.addCleanup(patcher.stop)
        self.service = ReservaService()

    def test_criar_reserva_adds_reserva_and_returns_it(self):
        cliente = "Cliente1"
        filme = "Filme1"
        qtd_ingressos = 2
        mock_reserva = MagicMock()
        self.mock_reserva_class.return_value = mock_reserva

        reserva = self.service.criar_reserva(cliente, filme, qtd_ingressos)

        self.mock_reserva_class.assert_called_once_with(cliente, filme, qtd_ingressos)
        self.assertIn(reserva, self.service.reservas)
        self.assertEqual(reserva, mock_reserva)

    def test_listar_returns_all_reservas(self):
        reserva1 = MagicMock()
        reserva2 = MagicMock()
        self.service.reservas = [reserva1, reserva2]
        self.assertEqual(self.service.listar(), [reserva1, reserva2])

    def test_buscar_por_cliente_returns_correct_reservas(self):
        cliente1 = "Cliente1"
        cliente2 = "Cliente2"
        reserva1 = MagicMock(cliente=cliente1)
        reserva2 = MagicMock(cliente=cliente2)
        reserva3 = MagicMock(cliente=cliente1)
        self.service.reservas = [reserva1, reserva2, reserva3]

        result = self.service.buscar_por_cliente(cliente1)
        self.assertEqual(result, [reserva1, reserva3])

    def test_remover_removes_reserva(self):
        reserva1 = MagicMock()
        reserva2 = MagicMock()
        self.service.reservas = [reserva1, reserva2]
        self.service.remover(reserva1)
        self.assertNotIn(reserva1, self.service.reservas)
        self.assertIn(reserva2, self.service.reservas)

    def test_remover_raises_valueerror_if_not_found(self):
        reserva1 = MagicMock()
        self.service.reservas = []
        with self.assertRaises(ValueError):
            self.service.remover(reserva1)

if __name__ == '__main__':
    unittest.main()