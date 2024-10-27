from src.repositorios.estrategias.estrategias_vendas import (
    EstrategiaVendasDB,
    EstrategiaVendasRAM,
)
from src.repositorios.gerenciadores.gerenciador_vendas import GerenciadorVendas
from src.repositorios.repositorios_vendas import RepositorioVendasDB, RepositorioVendasRAM

from .fabrica_abstrata import FabricaAbstrata


class FabricaGerenciadorVendas(FabricaAbstrata):
    _repositorios = {
        "ram": GerenciadorVendas(
            EstrategiaVendasRAM(RepositorioVendasRAM().pegar_repositorio())
        ),
        "db": GerenciadorVendas(
            EstrategiaVendasDB(RepositorioVendasDB().pegar_repositorio())
        ),
    }

    def criar(self, tipo: str):
        gerenciador = FabricaGerenciadorVendas._repositorios.get(tipo)
        return gerenciador
