from .entidade import Entidade

class Venda(Entidade):
    def __init__(self, id_: int,
                id_loja: int,
                id_vendedor: int,
                id_produto: int,
                quantidade: int,
                preco_total: float):
        super().__init__(id_)
        self.id_: int = id_
        self.id_loja: int = id_loja
        self.id_vendedor:int  = id_vendedor
        self.id_produto: int = id_produto
        self.quantidade: int = quantidade
        self.preco_total: float = preco_total

    def __str__(self):
        return f"[{self.id_}] ID vendedor: {self.id_vendedor}, ID do produto: {self.id_produto}, Quantidade: {self.quantidade},  Preco total: {self.preço_total}"