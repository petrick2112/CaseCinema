import pytest
from models.cliente import Cliente

def test_cliente_creation_sets_nome_and_email():
    cliente = Cliente(nome="João Silva", email="joao@email.com")
    assert cliente.nome == "João Silva"
    assert cliente.email == "joao@email.com"

def test_cliente_id_is_string_of_length_8():
    cliente = Cliente(nome="Maria", email="maria@email.com")
    assert isinstance(cliente.id, str)
    assert len(cliente.id) == 8

def test_cliente_id_is_unique():
    cliente1 = Cliente(nome="A", email="a@email.com")
    cliente2 = Cliente(nome="B", email="b@email.com")
    assert cliente1.id != cliente2.id