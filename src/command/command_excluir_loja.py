from src.command.command import Command


class ExcluirLojaCommand(Command):
    def __init__(self, gerenciador_lojas, id_loja):
        self.gerenciador_lojas = gerenciador_lojas
        self.id_loja = id_loja

    def execute(self):
        self.gerenciador_lojas.remover(self.id_loja)