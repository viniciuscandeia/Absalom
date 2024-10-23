from .entidade import Entidade


class Produto(Entidade):
    def __init__(self, id_: int,
                 nome: str,
                 tipo: str,
                 preco: float,
                 quantidade: int,
                 id_loja: int):
        super().__init__(id_, nome)
        self.tipo = tipo
        self.preco = preco
        self.quantidade = quantidade
        self.id_loja = id_loja

    def __str__(self):
        return f"[{self.id_}] Nome: {self.nome}, Tipo: {self.tipo}, Preco: {self.preco}, Quantidade: {self.quantidade}, Loja: {self.id_loja}"
