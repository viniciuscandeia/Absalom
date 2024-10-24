from src.entidades.entidade_loja import Loja
from ..estrategias.interface_estrategia import InterfaceEstrategia


class GerenciadorLojas:
    def __init__(self, estrategia: InterfaceEstrategia):
        self.estrategia = estrategia

    def adicionar(self, entidade: Loja):
        self.estrategia.adicionar(entidade)

    def remover(self, id_: int):
        self.estrategia.remover(id_)

    def editar(self, id_: int, entidade: Loja):
        self.estrategia.editar(id_, entidade)

    def buscar(self, id_: int):
        return self.estrategia.buscar(id_)

    def verificar_existencia(self, id_: int) -> bool:
        return self.estrategia.verificar_existencia(id_)

    def listar(self) -> dict:
        return self.estrategia.listar()

    def gerar_novo_id(self) -> int:
        return self.estrategia.gerar_novo_id()
