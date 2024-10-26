from src.entidades.entidade_loja import Loja

from ..estrategias.estrategias_lojas import InterfaceEstrategiaLojas

class GerenciadorLojas:
    def __init__(self, estrategia: InterfaceEstrategiaLojas):
        self.estrategia = estrategia

    def adicionar(self, loja: Loja):
        self.estrategia.adicionar(loja)

    def remover(self, id_loja: int):
        self.estrategia.remover(id_loja)

    def editar(self, id_loja: int, loja: Loja):
        self.estrategia.editar(id_loja, loja)

    def buscar(self, id_loja: int):
        return self.estrategia.buscar(id_loja)

    def verificar_existencia(self, id_loja: int) -> bool:
        return self.estrategia.verificar_existencia(id_loja)

    def listar(self) -> dict:
        return self.estrategia.listar()

    def gerar_novo_id(self) -> int:
        return self.estrategia.gerar_novo_id()
