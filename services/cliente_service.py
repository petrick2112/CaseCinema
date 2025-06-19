from models.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrar(self, nome, email):
        cliente = Cliente(nome, email)
        self.clientes.append(cliente)
        return cliente

    def listar(self):
        return self.clientes

    def buscar_por_id(self, cliente_id):
        return next((c for c in self.clientes if c.id == cliente_id), None)