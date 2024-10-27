from .comando import Comando

class EditarLojaComando(Comando):
    def __init__(self, gerenciador_lojas, id_loja: int, loja):
        self.gerenciador_lojas = gerenciador_lojas
        self.id_loja: int = id_loja
        self.loja = loja

    def execute(self):
        self.gerenciador_lojas.editar(self.id_loja, self.loja)