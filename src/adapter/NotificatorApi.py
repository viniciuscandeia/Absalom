from abc import ABC, abstractmethod

from src.entidades.entidade_notificacao import Notificacao


class NotificatorApi(ABC):

    @abstractmethod
    def send(self, notificacao: Notificacao):
        pass

    @abstractmethod
    def receive(id_loja, id_usuario) -> list[Notificacao]:
        pass
