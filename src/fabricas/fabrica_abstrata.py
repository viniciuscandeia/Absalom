from abc import ABC, abstractmethod


class FabricaAbstrata(ABC):

    @abstractmethod
    def criar(tipo: str):
        pass
