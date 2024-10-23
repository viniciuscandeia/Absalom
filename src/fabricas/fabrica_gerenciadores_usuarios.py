from ..repositorios.estrategias.estrategias_usuarios import (
    EstrategiaUsuariosDB,
    EstrategiaUsuariosRAM,
)
from ..repositorios.gerenciadores.gerenciador_usuarios import GerenciadorUsuarios
from ..repositorios.repositorios_usuarios import (
    RepositorioUsuariosDB,
    RepositorioUsuariosRAM,
)


class FabricaGerenciadorUsuarios:
    _repositorios = {
        "ram": GerenciadorUsuarios(
            EstrategiaUsuariosRAM(RepositorioUsuariosRAM().pegar_repositorio())
        ),
        "db": GerenciadorUsuarios(
            EstrategiaUsuariosDB(RepositorioUsuariosDB().pegar_repositorio())
        ),
    }

    @staticmethod
    def criar_gerenciador(tipo: str):
        gerenciador = FabricaGerenciadorUsuarios._repositorios.get(tipo)
        if gerenciador:
            return gerenciador
        else:
            raise ValueError(f"Tipo de persistência desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Gerenciadores de Usuários"
