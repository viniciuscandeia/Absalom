from .entidade import Entidade


class Loja(Entidade):
    def __init__(self, id_: int, nome: str, endereco: str):
        super().__init__(id_, nome)
        self.endereco = endereco

    def __str__(self):
        return f"[{self.id_}] Nome: {self.nome}, Endereco: {self.endereco}"
