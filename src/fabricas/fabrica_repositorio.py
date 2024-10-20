from abc import abstractmethod, ABC

class FabricaRepositorio(ABC):
    def criar_repositorio(self, tipo: str):
        pass
