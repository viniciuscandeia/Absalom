from .comando import Comando
from ..adapter.notification.NotificatorApiSingleton import NotificatorApiSingleton
from ..entidades.entidade_notificacao import Notificacao


class VerNotificacoesComando(Comando):
    def __init__(self, id_loja:int):
        self.id_loja = id_loja
        self.notificatorApi = NotificatorApiSingleton()

    def execute(self) -> list[Notificacao]:
        return self.notificatorApi.notificator.receive(self.id_loja)