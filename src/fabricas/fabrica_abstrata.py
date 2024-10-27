from abc import ABC, abstractmethod


class FabricaAbstrata(ABC):

    @abstractmethod
    def criar(self, tipo: str):
        pass
