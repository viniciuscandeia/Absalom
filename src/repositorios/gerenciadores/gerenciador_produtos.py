from src.entidades.entidade_produto import Produto
from ..estrategias.interface_estrategia import InterfaceEstrategia


class GerenciadorProdutos:
    def __init__(self, estrategia: InterfaceEstrategia):
        self.estrategia = estrategia

    def adicionar(self, entidade: Produto):
        self.estrategia.adicionar(entidade)

    def remover(self, id_: int):
        self.estrategia.remover(id_)

    def editar(self, id_: int, entidade: Produto):
        self.estrategia.editar(id_, entidade)

    def buscar(self, id_: int):
        return self.estrategia.buscar(id_)

    def listar(self) -> dict:
        return self.estrategia.listar()
