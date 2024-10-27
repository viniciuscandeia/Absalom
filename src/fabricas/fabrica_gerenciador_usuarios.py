from ..repositorios.estrategias.estrategias_usuarios import (
    EstrategiaUsuariosDB,
    EstrategiaUsuariosRAM,
)
from ..repositorios.gerenciadores.gerenciador_usuarios import GerenciadorUsuarios
from ..repositorios.repositorios_usuarios import (
    RepositorioUsuariosDB,
    RepositorioUsuariosRAM,
)
from .fabrica_abstrata import FabricaAbstrata


class FabricaGerenciadorUsuarios(FabricaAbstrata):
    _repositorios = {
        "ram": GerenciadorUsuarios(
            EstrategiaUsuariosRAM(RepositorioUsuariosRAM().pegar_repositorio())
        ),
        "db": GerenciadorUsuarios(
            EstrategiaUsuariosDB(RepositorioUsuariosDB().pegar_repositorio())
        ),
    }

    def criar(self, tipo: str):
        gerenciador = FabricaGerenciadorUsuarios._repositorios.get(tipo)
        return gerenciador
