import uuid

class Cliente:
    def __init__(self, nome, email):
        self.id = str(uuid.uuid4())[:8]
        self.nome = nome
        self.email = email