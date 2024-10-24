from .entidade import Entidade


class Produto(Entidade):
    def __init__(self, id_: int,
                 nome: str,
                 descricao: str,
                 preco: float,
                 quantidade: int,
                 id_loja: int):
        super().__init__(id_)
        self.nome: str = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.id_loja = id_loja

    def __str__(self):
        return f"[{self.id_}] Nome: {self.nome}, Descrição: {self.descricao}, Preco: {self.preco}, Quantidade: {self.quantidade}, Loja: {self.id_loja}"
