from abc import ABC, abstractmethod

from ..repositorios.estrategias.gerenciador_repositorio_usuarios import GerenciadorRepositorioUsuarios
from ..repositorios.estrategias.estrategias_gerenciamento_usuarios import GerenciamentoUsuariosRAM, GerenciamentoUsuariosDB
from ..repositorios.repositorios_usuarios import RepositorioUsuariosRAM, RepositorioUsuariosDB


class FabricaRepositorioUsuario(ABC):
    @abstractmethod
    def criar_repositorio(self, tipo: str):
        pass


class FabricaRepositoriosUsuarios(FabricaRepositorioUsuario):
    _repositorios = {
        'ram': RepositorioUsuariosRAM,
        'db': RepositorioUsuariosDB
    }

    @staticmethod
    def criar_repositorio(tipo: str):
        repositorio_class = FabricaRepositoriosUsuarios._repositorios.get(
            tipo)
        if repositorio_class:
            return repositorio_class().pegar_repositorio()
        else:
            raise ValueError(f"Tipo de repositório desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Repositórios de Usuários"


class FabricaGerenciadorRepositorioUsuarios:
    _repositorios = {
        'ram': GerenciadorRepositorioUsuarios(GerenciamentoUsuariosRAM(RepositorioUsuariosRAM().pegar_repositorio())),
        'db': GerenciadorRepositorioUsuarios(GerenciamentoUsuariosDB(RepositorioUsuariosDB().pegar_repositorio()))
    }

    @staticmethod
    def criar_gerenciador(tipo: str):
        gerenciador = FabricaGerenciadorRepositorioUsuarios._repositorios.get(
            tipo)
        if gerenciador:
            return gerenciador
        else:
            raise ValueError(f"Tipo de persistência desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Gerenciadores de Repositórios dos Usuários"
