import unittest
from unittest.mock import patch, MagicMock
from main import menu
from main import cadastrar_cliente
from main import listar_clientes
from main import fazer_reserva
from main import fazer_reserva
from main import comprar_ingresso
from main import comprar_ingresso
from main import listar_reservas
from main import listar_compras

# test_main.py


class TestMenu(unittest.TestCase):
    @patch("builtins.input", side_effect=["0"])
    @patch("builtins.print")
    def test_menu_exit(self, mock_print, mock_input):
        menu()
        mock_print.assert_any_call("Sistema finalizado")

    @patch("builtins.input", side_effect=["9", "0"])
    @patch("builtins.print")
    def test_menu_invalid_option(self, mock_print, mock_input):
        menu()
        mock_print.assert_any_call("Erro! opção inválida!\n")
        mock_print.assert_any_call("Sistema finalizado")

    @patch("main.cadastrar_cliente")
    @patch("builtins.input", side_effect=["1", "0"])
    @patch("builtins.print")
    def test_menu_cadastrar_cliente(self, mock_print, mock_input, mock_cadastrar):
        menu()
        self.assertTrue(mock_cadastrar.called)
        mock_print.assert_any_call("Sistema finalizado")

    @patch("main.listar_clientes")
    @patch("builtins.input", side_effect=["2", "0"])
    @patch("builtins.print")
    def test_menu_listar_clientes(self, mock_print, mock_input, mock_listar):
        menu()
        self.assertTrue(mock_listar.called)
        mock_print.assert_any_call("Sistema finalizado")

    @patch("main.fazer_reserva")
    @patch("builtins.input", side_effect=["3", "0"])
    @patch("builtins.print")
    def test_menu_fazer_reserva(self, mock_print, mock_input, mock_fazer):
        menu()
        self.assertTrue(mock_fazer.called)
        mock_print.assert_any_call("Sistema finalizado")

    @patch("main.comprar_ingresso")
    @patch("builtins.input", side_effect=["4", "0"])
    @patch("builtins.print")
    def test_menu_comprar_ingresso(self, mock_print, mock_input, mock_comprar):
        menu()
        self.assertTrue(mock_comprar.called)
        mock_print.assert_any_call("Sistema finalizado")

    @patch("main.listar_reservas")
    @patch("builtins.input", side_effect=["5", "0"])
    @patch("builtins.print")
    def test_menu_listar_reservas(self, mock_print, mock_input, mock_listar):
        menu()
        self.assertTrue(mock_listar.called)
        mock_print.assert_any_call("Sistema finalizado")

    @patch("main.listar_compras")
    @patch("builtins.input", side_effect=["6", "0"])
    @patch("builtins.print")
    def test_menu_listar_compras(self, mock_print, mock_input, mock_listar):
        menu()
        self.assertTrue(mock_listar.called)
        mock_print.assert_any_call("Sistema finalizado")

        @patch("main.cliente_service")
        @patch("main.logger")
        @patch("builtins.input", side_effect=["João", "joao@email.com"])
        @patch("builtins.print")
        def test_cadastrar_cliente(self, mock_print, mock_input, mock_logger, mock_cliente_service):
            mock_cliente = MagicMock()
            mock_cliente.id = 1
            mock_cliente.nome = "João"
            mock_cliente.email = "joao@email.com"
            mock_cliente_service.cadastrar.return_value = mock_cliente

            cadastrar_cliente()
            mock_cliente_service.cadastrar.assert_called_with("João", "joao@email.com")
            mock_logger.info.assert_called()
            mock_print.assert_any_call("Cliente cadastrado com ID: 1\n")

        @patch("main.cliente_service")
        @patch("main.logger")
        @patch("builtins.print")
        def test_listar_clientes(self, mock_print, mock_logger, mock_cliente_service):
            mock_cliente = MagicMock()
            mock_cliente.id = 1
            mock_cliente.nome = "Maria"
            mock_cliente.email = "maria@email.com"
            mock_cliente_service.listar.return_value = [mock_cliente]

            listar_clientes()
            mock_logger.info.assert_called_with("Listando clientes")
            mock_print.assert_any_call("\n### Clientes ###")
            mock_print.assert_any_call("1 - Maria (maria@email.com)")

        @patch("main.cliente_service")
        @patch("main.reserva_service")
        @patch("main.logger")
        @patch("builtins.input", side_effect=["1", "Filme X", "2"])
        @patch("main.listar_clientes")
        @patch("builtins.print")
        def test_fazer_reserva_success(self, mock_print, mock_listar, mock_input, mock_logger, mock_reserva_service, mock_cliente_service):
            mock_cliente = MagicMock()
            mock_cliente.id = "1"
            mock_cliente.nome = "Carlos"
            mock_cliente_service.buscar_por_id.return_value = mock_cliente
            mock_reserva = MagicMock()
            mock_reserva.id = 10
            mock_reserva.cliente = mock_cliente
            mock_reserva_service.criar_reserva.return_value = mock_reserva

            fazer_reserva()
            mock_reserva_service.criar_reserva.assert_called_with(mock_cliente, "Filme X", 2)
            mock_logger.info.assert_called()
            mock_print.assert_any_call("Reserva realizada com ID: 10\n")

        @patch("main.cliente_service")
        @patch("main.logger")
        @patch("builtins.input", side_effect=["999"])
        @patch("main.listar_clientes")
        @patch("builtins.print")
        def test_fazer_reserva_cliente_nao_encontrado(self, mock_print, mock_listar, mock_input, mock_logger, mock_cliente_service):
            mock_cliente_service.buscar_por_id.return_value = None

            fazer_reserva()
            mock_logger.warning.assert_called()
            mock_print.assert_any_call("Cliente não encontrado.\n")

        @patch("main.cliente_service")
        @patch("main.reserva_service")
        @patch("main.compra_service")
        @patch("main.produto_service")
        @patch("main.logger")
        @patch("builtins.input", side_effect=["1", "", "Filme Y", "3", "", ""])
        @patch("main.listar_clientes")
        @patch("builtins.print")
        def test_comprar_ingresso_sem_reserva(self, mock_print, mock_listar, mock_input, mock_logger, mock_produto_service, mock_compra_service, mock_reserva_service, mock_cliente_service):
            mock_cliente = MagicMock()
            mock_cliente.id = "1"
            mock_cliente.nome = "Ana"
            mock_cliente_service.buscar_por_id.return_value = mock_cliente
            mock_reserva_service.buscar_por_cliente.return_value = []
            mock_compra = MagicMock()
            mock_compra.id = 5
            mock_compra.total.return_value = 50.0
            mock_compra.produtos = []
            mock_compra_service.criar_compra.return_value = mock_compra
            mock_produto_service.listar.return_value = []

            comprar_ingresso()
            mock_logger.info.assert_any_call("Compra criada: 5 para cliente 1")
            mock_print.assert_any_call("\nCompra realizada com ID: 5")
            mock_print.assert_any_call("Total: R$50.00\n")

        @patch("main.reserva_service")
        @patch("main.logger")
        @patch("main.cliente_service")
        @patch("builtins.input", side_effect=["1"])
        @patch("main.listar_clientes")
        @patch("builtins.print")
        def test_comprar_ingresso_cliente_nao_encontrado(self, mock_print, mock_listar, mock_input, mock_cliente_service, mock_logger, mock_reserva_service):
            mock_cliente_service.buscar_por_id.return_value = None

            comprar_ingresso()
            mock_logger.warning.assert_called()
            mock_print.assert_any_call("Cliente não encontrado.\n")

        @patch("main.reserva_service")
        @patch("main.logger")
        @patch("builtins.print")
        def test_listar_reservas(self, mock_print, mock_logger, mock_reserva_service):
            mock_cliente = MagicMock()
            mock_cliente.nome = "Pedro"
            mock_reserva = MagicMock()
            mock_reserva.id = 2
            mock_reserva.cliente = mock_cliente
            mock_reserva.filme = "Filme Z"
            mock_reserva.qtd_ingressos = 4
            mock_reserva_service.listar.return_value = [mock_reserva]

            listar_reservas()
            mock_logger.info.assert_called_with("Listando reservas")
            mock_print.assert_any_call("ID: 2 | Cliente: Pedro | Filme: Filme Z | Qtd: 4")

        @patch("main.compra_service")
        @patch("main.logger")
        @patch("builtins.print")
        def test_listar_compras(self, mock_print, mock_logger, mock_compra_service):
            mock_cliente = MagicMock()
            mock_cliente.nome = "Lucas"
            mock_compra = MagicMock()
            mock_compra.id = 3
            mock_compra.cliente = mock_cliente
            mock_compra.filme = "Filme W"
            mock_compra.qtd_ingressos = 2
            mock_produto = MagicMock()
            mock_produto.nome = "Pipoca"
            mock_produto.preco = 10.0
            mock_compra.produtos = [(mock_produto, 2)]
            mock_compra.total.return_value = 30.0
            mock_compra_service.listar.return_value = [mock_compra]

            listar_compras()
            mock_logger.info.assert_called_with("Listando compras")
            mock_print.assert_any_call("Compra 3 - Cliente: Lucas - Filme: Filme W")
            mock_print.assert_any_call("Ingressos: 2")
            mock_print.assert_any_call("Produtos:")
            mock_print.assert_any_call("  - Pipoca x2 = R$20.00")
            mock_print.assert_any_call("Total: R$30.00\n")

if __name__ == "__main__":
    unittest.main()