from abc import ABC, abstractmethod


class FabricaRepositorio(ABC):

    @abstractmethod
    def criar_repositorio(self, tipo: str):
        pass
