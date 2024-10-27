from src.repositorios.estrategias.estrategias_lojas import (
    EstrategiaLojasDB,
    EstrategiaLojasRAM,
)
from src.repositorios.gerenciadores.gerenciador_lojas import GerenciadorLojas
from src.repositorios.repositorios_lojas import RepositorioLojasDB, RepositorioLojasRAM

from .fabrica_abstrata import FabricaAbstrata


class FabricaGerenciadorLojas(FabricaAbstrata):
    _repositorios = {
        "ram": GerenciadorLojas(
            EstrategiaLojasRAM(RepositorioLojasRAM().pegar_repositorio())
        ),
        "db": GerenciadorLojas(
            EstrategiaLojasDB(RepositorioLojasDB().pegar_repositorio())
        ),
    }

    def criar(self, tipo: str):
        gerenciador = FabricaGerenciadorLojas._repositorios.get(tipo)
        return gerenciador

