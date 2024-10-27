from .comando import Comando


class ExcluirProdutoComando(Comando):
    def __init__(self, gerenciador_produtos, id_produto: int):
        self.gerenciador_produtos = gerenciador_produtos
        self.id_produto: int = id_produto

    def execute(self):
        self.gerenciador_produtos.remover(self.id_produto)
