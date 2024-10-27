from src.repositorios.estrategias.estrategias_notificacoes import (
    EstrategiaNotificacoesDB,
    EstrategiaNotificacoesFirebase,
)
from src.repositorios.gerenciadores.gerenciador_notificacoes import (
    GerenciadorNotificacoes,
)
from src.repositorios.repositorio_notificacoes import (
    RepositorioNotificacoesDB,
    RepositorioNotificacoesFirebase,
)

from .fabrica_abstrata import FabricaAbstrata


class FabricaGerenciadorNotificacoes(FabricaAbstrata):
    _repositorios = {
        "firebase": GerenciadorNotificacoes(
            EstrategiaNotificacoesFirebase(
                RepositorioNotificacoesFirebase().pegar_repositorio()
            )
        ),
        "db": GerenciadorNotificacoes(
            EstrategiaNotificacoesDB(RepositorioNotificacoesDB().pegar_repositorio())
        ),
    }

    def criar(self, tipo: str):
        gerenciador = FabricaGerenciadorNotificacoes._repositorios.get(tipo)
        return gerenciador
