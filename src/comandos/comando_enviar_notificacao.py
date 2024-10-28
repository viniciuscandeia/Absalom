from ..adapter.notification.NotificatorApiSingleton import NotificatorApiSingleton
from .comando import Comando


class EnviarNotificacaoComando(Comando):
    def __init__(self, loja, id_usuario: int):
        self.loja = loja
        self.id_usuario = id_usuario
        self.notificatorApi = NotificatorApiSingleton()

    def execute(self):
        (
            self.notificatorApi.build_send_notificacao(
                id_usuario=self.id_usuario, loja=self.loja
            )
        )
