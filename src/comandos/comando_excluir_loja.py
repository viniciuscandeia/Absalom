from .comando import Comando


class ExcluirLojaComando(Comando):
    def __init__(self, gerenciador_lojas, id_loja: int):
        self.gerenciador_lojas = gerenciador_lojas
        self.id_loja: int = id_loja

    def execute(self):
        self.gerenciador_lojas.remover(self.id_loja)
