from src.command.command import Command

class AdicionarProdutoCommand(Command):
    def __init__(self, gerenciador_produtos, produto):
        self.gerenciador_produtos = gerenciador_produtos
        self.produto = produto

    def execute(self):
        self.gerenciador_produtos.adicionar(self.produto)