from .entidade import Entidade


class Loja(Entidade):
    def __init__(self, id_: int, nome: str, endereco: str):
        super().__init__(id_)
        self.nome: str = nome
        self.endereco: str = endereco

    def __str__(self):
        return f"[{self.id_}] Nome: {self.nome}, Endereço: {self.endereco}"
