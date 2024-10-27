from .comando import Comando

class EditarLojaComando(Comando):
    def __init__(self, gerenciador_lojas,  loja, id_usuario:int):
        self.gerenciador_lojas = gerenciador_lojas
        self.loja = loja
        self.id_usuario = id_usuario

    def execute(self):
        self.gerenciador_lojas.editar(self.id_usuario, self.loja)
