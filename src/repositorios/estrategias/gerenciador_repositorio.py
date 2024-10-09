from .estrategias_gerenciamento_usuarios import GerenciamentoEstrategia
from ...entidades.entidades_usuarios import Usuario

class GerenciadorRepositorio:
    def __init__(self, estrategia: GerenciamentoEstrategia):
        self.estrategia = estrategia

    def adicionar(self, id_: int, usuario: Usuario):
        self.estrategia.adicionar(id_, usuario)

    def remover(self, id_: int):
        self.estrategia.remover(id_)

    def editar(self, id_: int, usuario: Usuario):
        self.estrategia.editar(id_, usuario)

    def buscar(self, id_: int):
        return self.estrategia.buscar(id_)

    def listar(self, tipo: str = None, id_loja: int = None) -> list[Usuario]:
        return self.estrategia.listar(tipo, id_loja)
