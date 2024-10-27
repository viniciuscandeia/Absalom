from src.command.command import Command

class ExcluirProdutoCommand(Command):
    def __init__(self, gerenciador_produtos, id_loja):
        self.gerenciador_produtos = gerenciador_produtos
        self.id_loja = id_loja

    def execute(self):
        self.gerenciador_produtos.remover(self.id_loja)