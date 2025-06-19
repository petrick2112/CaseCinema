import pytest
from models.reserva import Reserva

class Dummy:
    pass

def test_reserva_initialization():
    cliente = Dummy()
    filme = Dummy()
    qtd_ingressos = 3

    reserva = Reserva(cliente, filme, qtd_ingressos)

    assert isinstance(reserva.id, str)
    assert len(reserva.id) == 8
    assert reserva.cliente is cliente
    assert reserva.filme is filme
    assert reserva.qtd_ingressos == qtd_ingressos

def test_reserva_unique_id():
    cliente = Dummy()
    filme = Dummy()
    reserva1 = Reserva(cliente, filme, 1)
    reserva2 = Reserva(cliente, filme, 2)
    assert reserva1.id != reserva2.id