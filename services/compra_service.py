from models.compra import Compra

class CompraService:
    def __init__(self):
        self.compras = []

    def criar_compra(self, cliente, filme, qtd_ingressos):
        compra = Compra(cliente, filme, qtd_ingressos)
        self.compras.append(compra)
        return compra

    def listar(self):
        return self.compras