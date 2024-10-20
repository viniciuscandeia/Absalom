from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class GerenciamentoEstrategia(ABC, Generic[T]):
    @abstractmethod
    def adicionar(self, entidade: T):
        pass

    @abstractmethod
    def remover(self, id_: int):
        pass

    @abstractmethod
    def editar(self, id_: int, entidade: T):
        pass

    @abstractmethod
    def buscar(self, id_: int):
        pass

    @abstractmethod
    def _existe(self, id_: int):
        pass

    @abstractmethod
    def listar(*args, **kwargs):
        pass

