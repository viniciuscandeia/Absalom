from src.adapter.NotificatorApi import NotificatorApi
from src.entidades.entidade_notificacao import Notificacao
from src.fabricas.fabrica_gerenciador_notificacoes import FabricaGerenciadorNotificacoes


class DatabaseAdapterNotificatorApi(NotificatorApi):
    def __init__(self):
        super().__init__()
        self.gerenciador_notificacoes = FabricaGerenciadorNotificacoes().criar(
            tipo='db'
        )

    def send(self, notificacao: Notificacao):
        self.gerenciador_notificacoes.send(notificacao)

    def receive(self, id_loja):
        return self.gerenciador_notificacoes.receive(id_loja)
