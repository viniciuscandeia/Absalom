from uuid import uuid4


class Loja:
    def __init__(self, id_ = None, nome = "", endereco = ""):
        self.id_ = id_ if id_ else uuid4().hex
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"[{self.id_}] Nome: {self.nome}, Endereco: {self.endereco}"