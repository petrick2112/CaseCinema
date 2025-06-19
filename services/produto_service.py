from models.produto import Produto

class ProdutoService:
    def __init__(self):
        self.produtos = [
            Produto("Pipoca", 10.0),
            Produto("Chocolate", 7.0),
            Produto("Refrigerante", 6.0),
        ]

    def listar(self):
        return self.produtos