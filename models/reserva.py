import uuid

class Reserva:
    def __init__(self, cliente, filme, qtd_ingressos):
        self.id = str(uuid.uuid4())[:8]
        self.cliente = cliente
        self.filme = filme
        self.qtd_ingressos = qtd_ingressos