class Produto:
    def __init__(self, id_ = None,
                nome = "",
                tipo = "",
                preco = 0.0,
                quantidade = 0,
                id_loja = None):
        self.id_ = id_
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.quantidade = quantidade
        self.id_loja = id_loja

    def __str__(self):
        return f"[{self.id_}] Nome: {self.nome}, Tipo: {self.tipo}, Preco: {self.preco}, Quantidade: {self.quantidade}, Loja: {self.id_loja}"