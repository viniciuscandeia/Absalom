from src.entidades.entidade_venda import Venda
from src.repositorios.estrategias.estrategias_vendas import InterfaceEstrategiaVendas


class GerenciadorVendas:
    def __init__(self, estrategia: InterfaceEstrategiaVendas):
        self.estrategia = estrategia

    def adicionar(self, venda: Venda):
        self.estrategia.adicionar(venda)

    def remover(self, id_venda: int):
        self.estrategia.remover(id_venda)

    def buscar(self, id_venda: int):
        return self.estrategia.buscar(id_venda)

    def listar(self, id_loja: int = None) -> dict:
        return self.estrategia.listar(id_loja)

    def gerar_novo_id(self) -> int:
        return self.estrategia.gerar_novo_id()
