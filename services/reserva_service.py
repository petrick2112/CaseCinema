from models.reserva import Reserva

class ReservaService:
    def __init__(self):
        self.reservas = []

    def criar_reserva(self, cliente, filme, qtd_ingressos):
        reserva = Reserva(cliente, filme, qtd_ingressos)
        self.reservas.append(reserva)
        return reserva

    def listar(self):
        return self.reservas

    def buscar_por_cliente(self, cliente):
        return [r for r in self.reservas if r.cliente == cliente]

    def remover(self, reserva):
        self.reservas.remove(reserva)