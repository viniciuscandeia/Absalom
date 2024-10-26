from src.fabricas.fabrica_repositorio import FabricaRepositorio
from src.repositorios.estrategias.estrategias_notificacoes import EstrategiaNotificacoesFirebase, \
    EstrategiaNotificacoesDB
from src.repositorios.gerenciadores.gerenciador_notificacoes import GerenciadorNotificacoes
from src.repositorios.repositorio_notificacoes import RepositorioNotificacoesFirebase, RepositorioNotificacoesDB


class FabricaRepositoriosNotificacoes(FabricaRepositorio):
    _repositorios = {
        'ram': RepositorioNotificacoesFirebase,
        'db': RepositorioNotificacoesDB
    }

    @staticmethod
    def criar_repositorio(tipo: str):
        repositorio_class = FabricaRepositoriosNotificacoes._repositorios.get(
            tipo)
        if repositorio_class:
            return repositorio_class().pegar_repositorio()
        else:
            raise ValueError(f"Tipo de repositório desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Repositórios de Notificacoes"



class FabricaGerenciadorNotificacoes:
    _repositorios = {
        'firebase': GerenciadorNotificacoes(EstrategiaNotificacoesFirebase(RepositorioNotificacoesFirebase().pegar_repositorio())),
        'db': GerenciadorNotificacoes(EstrategiaNotificacoesDB(RepositorioNotificacoesDB().pegar_repositorio()))
    }

    @staticmethod
    def criar_gerenciador(tipo: str):
        gerenciador = FabricaGerenciadorNotificacoes._repositorios.get(
            tipo)
        if gerenciador:
            return gerenciador
        else:
            raise ValueError(f"Tipo de persistência desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Gerenciadores de Repositórios das Lojas"
