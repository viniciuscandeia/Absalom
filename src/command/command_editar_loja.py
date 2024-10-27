from src.command.command import Command

class EditarLojaCommand(Command):
    def __init__(self, gerenciador_lojas, id_loja, loja):
        self.gerenciador_lojas = gerenciador_lojas
        self.id_loja = id_loja
        self.loja = loja

    def execute(self):
        self.gerenciador_lojas.editar(self.id_loja, self.loja)