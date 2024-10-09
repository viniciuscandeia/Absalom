from abc import ABC, abstractmethod

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
