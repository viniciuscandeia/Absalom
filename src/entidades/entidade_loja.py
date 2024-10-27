from .entidade import Entidade


class Loja(Entidade):
    def __init__(self, id_: int, nome: str, endereco: str):
        super().__init__(id_)
        self.nome: str = nome
        self.endereco: str = endereco

    def setNome(self, nome: str):
        self.nome = nome
        return self

    def setEndereco(self, endereco: str):
        self.endereco = endereco
        return self

    def toDict(self):
        informacoes: dict = {}
        informacoes["id"] = self.id_
        informacoes["nome"] = self.nome
        informacoes["endereco"] = self.endereco
        return informacoes

    def __str__(self):
        return f"[{self.id_}] Nome: {self.nome}, Endereço: {self.endereco}"
