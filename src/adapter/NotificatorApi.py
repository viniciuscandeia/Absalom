from abc import ABC, abstractmethod

from src.entidades.entidade_notificacao import Notificacao


class NotificatorApi(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def send(self, notificacao: Notificacao):
        pass

    @abstractmethod
    def receive(id_loja, id_usuario):
        pass
