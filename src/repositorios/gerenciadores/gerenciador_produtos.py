from src.entidades.entidade_produto import Produto
from src.repositorios.estrategias.estrategias_produtos import InterfaceEstrategiaProdutos


class GerenciadorProdutos:
    def __init__(self, estrategia: InterfaceEstrategiaProdutos):
        self.estrategia = estrategia

    def adicionar(self, produto: Produto):
        self.estrategia.adicionar(produto)

    def remover(self, id_produto: int):
        self.estrategia.remover(id_produto)

    def editar(self, id_produto: int, produto: Produto):
        self.estrategia.editar(id_produto, produto)

    def buscar(self, id_produto: int):
        return self.estrategia.buscar(id_produto)

    def listar(self, id_loja: int = None) -> dict:
        return self.estrategia.listar(id_loja)

    def gerar_novo_id(self) -> int:
        return self.estrategia.gerar_novo_id()

    def gerar_novo_id(self) -> int:
        return self.estrategia.gerar_novo_id()
