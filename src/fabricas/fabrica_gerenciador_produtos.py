from src.repositorios.estrategias.estrategias_produtos import (
    EstrategiaProdutosDB,
    EstrategiaProdutosRAM,
)
from src.repositorios.repositorio_produtos import (
    RepositorioProdutosDB,
    RepositorioProdutosRAM,
)

from ..repositorios.gerenciadores.gerenciador_produtos import GerenciadorProdutos
from .fabrica_abstrata import FabricaAbstrata


class FabricaGerenciadorProdutos(FabricaAbstrata):
    _repositorios = {
        "ram": GerenciadorProdutos(
            EstrategiaProdutosRAM(RepositorioProdutosRAM().pegar_repositorio())
        ),
        "db": GerenciadorProdutos(
            EstrategiaProdutosDB(RepositorioProdutosDB().pegar_repositorio())
        ),
    }

    def criar(self, tipo: str):
        gerenciador = FabricaGerenciadorProdutos._repositorios.get(tipo)
        return gerenciador
