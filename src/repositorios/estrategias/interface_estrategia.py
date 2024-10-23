from abc import ABC, abstractmethod

from ...entidades.entidade import Entidade


class InterfaceEstrategia(ABC):
    @abstractmethod
    def adicionar(self, entidade: Entidade):
        pass

    @abstractmethod
    def remover(self, id_: int):
        pass

    @abstractmethod
    def editar(self, id_: int, entidade: Entidade):
        pass

    @abstractmethod
    def verificar_existencia(self, id_: int):
        pass

    @abstractmethod
    def buscar(self, id_: int):
        pass

    @abstractmethod
    def listar(*args, **kwargs):
        pass

    @abstractmethod
    def gerar_novo_id(self):
        pass
