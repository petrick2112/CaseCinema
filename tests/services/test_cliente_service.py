import pytest
from services.cliente_service import ClienteService
from models.cliente import Cliente

class DummyCliente(Cliente):
    _id_counter = 1
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.id = DummyCliente._id_counter
        DummyCliente._id_counter += 1

@pytest.fixture(autouse=True)
def patch_cliente(monkeypatch):
    monkeypatch.setattr('services.cliente_service.Cliente', DummyCliente)
    DummyCliente._id_counter = 1

def test_cadastrar_cliente():
    service = ClienteService()
    cliente = service.cadastrar("João", "joao@email.com")
    assert isinstance(cliente, Cliente)
    assert cliente.nome == "João"
    assert cliente.email == "joao@email.com"
    assert cliente in service.clientes

def test_listar_clientes():
    service = ClienteService()
    service.cadastrar("Maria", "maria@email.com")
    service.cadastrar("Ana", "ana@email.com")
    clientes = service.listar()
    assert len(clientes) == 2
    assert clientes[0].nome == "Maria"
    assert clientes[1].nome == "Ana"

def test_buscar_por_id_encontrado():
    service = ClienteService()
    c1 = service.cadastrar("Carlos", "carlos@email.com")
    c2 = service.cadastrar("Pedro", "pedro@email.com")
    found = service.buscar_por_id(c2.id)
    assert found is c2

def test_buscar_por_id_nao_encontrado():
    service = ClienteService()
    service.cadastrar("Lucas", "lucas@email.com")
    result = service.buscar_por_id(999)
    assert result is None