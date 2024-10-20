from src.entidades.entidade_loja import Loja
from src.repositorios.estrategias.gerenciamento_estrategia import GerenciamentoEstrategia


class GerenciadorRepositorioLoja:
    def __init__(self, estrategia: GerenciamentoEstrategia[Loja]):
        self.estrategia = estrategia

    def adicionar(self, entidade: Loja):
        self.estrategia.adicionar(entidade)

    def remover(self, id_: int):
        self.estrategia.remover(id_)

    def editar(self, id_: int, entidade: Loja):
        self.estrategia.editar(id_, entidade)

    def buscar(self, id_: int):
        return self.estrategia.buscar(id_)

    def listar(self) -> list[Loja]:
        return self.estrategia.listar()
