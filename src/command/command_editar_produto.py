from src.command.command import Command

class EditarProdutoCommand(Command):
    def __init__(self, gerenciador_produtos, id_produto, produto):
        self.gerenciador_produtos = gerenciador_produtos
        self.id_produto = id_produto
        self.produto = produto

    def execute(self):
        self.gerenciador_produtos.editar(self.id_produto, self.produto)