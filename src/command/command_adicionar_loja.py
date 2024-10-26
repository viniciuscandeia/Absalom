from src.command.command import Command


class AdicionarLojaCommand(Command):
    def __init__(self, gerenciador_lojas, loja):
        self.gerenciador_lojas = gerenciador_lojas
        self.loja = loja

    def execute(self):
        self.gerenciador_lojas.adicionar(self.loja)
