from .comando import Comando

class EditarProdutoComando(Comando):
    def __init__(self, gerenciador_produtos, id_produto: int, produto):
        self.gerenciador_produtos = gerenciador_produtos
        self.id_produto: int = id_produto
        self.produto = produto

    def execute(self):
        self.gerenciador_produtos.editar(self.id_produto, self.produto)