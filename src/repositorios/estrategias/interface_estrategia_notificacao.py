from abc import ABC, abstractmethod

from ...entidades.entidade import Entidade
from ...entidades.entidade_notificacao import Notificacao


class InterfaceEstrategiaNotificacao(ABC):
    @abstractmethod
    def send(self, entidade: Notificacao):
        pass

    @abstractmethod
    def receive(self, id_loja: int):
        pass