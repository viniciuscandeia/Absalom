from .estrategias_gerenciamento_usuarios import GerenciamentoEstrategia
from ...entidades.entidades_usuarios import Usuario

class GerenciadorRepositorioUsuarios:
    def __init__(self, estrategia: GerenciamentoEstrategia[Usuario]):
        self.estrategia = estrategia

    def adicionar(self, entidade: Usuario):
        self.estrategia.adicionar(entidade)

    def remover(self, id_: int):
        self.estrategia.remover(id_)

    def editar(self, id_: int, entidade: Usuario):
        self.estrategia.editar(id_, entidade)

    def buscar(self, id_: int):
        return self.estrategia.buscar(id_)

    def listar(self, tipo: str = None, id_loja: int = None) -> list[Usuario]:
        return self.estrategia.listar(tipo, id_loja)

    def validar(self, username: str, senha: str) -> Usuario:
        return self.estrategia.validar(username, senha)