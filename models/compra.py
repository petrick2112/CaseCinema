import uuid

class Compra:
    def __init__(self, cliente, filme, qtd_ingressos):
        self.id = str(uuid.uuid4())[:8]
        self.cliente = cliente
        self.filme = filme
        self.qtd_ingressos = qtd_ingressos
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        self.produtos.append((produto, quantidade))

    def total(self):
        total_ingressos = self.qtd_ingressos * 25.0
        total_produtos = sum(p[0].preco * p[1] for p in self.produtos)
        return total_ingressos + total_produtos