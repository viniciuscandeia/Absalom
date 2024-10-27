from .comando import Comando
from ..adapter.notification.NotificatorApiSingleton import NotificatorApiSingleton


class EnviarNotificacaoComando(Comando):
    def __init__(self, loja, id_usuario:int):
        self.loja = loja
        self.id_usuario = id_usuario
        self.notificatorApi = NotificatorApiSingleton()

    def execute(self):
        (self.notificatorApi
         .build_send_notificacao(id_usuario=self.id_usuario, loja=self.loja))