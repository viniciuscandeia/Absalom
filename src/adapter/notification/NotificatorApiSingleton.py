from src.adapter.notification.DatabaseAdapterNotificatorApi import DatabaseAdapterNotificatorApi
from src.entidades.entidade_loja import Loja
from src.entidades.entidade_notificacao import Notificacao
from src.execoes.NotificationError import NotificationError
from src.fabricas.fabrica_entidades import FabricaEntidades


class NotificatorApiSingleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls.notificator = DatabaseAdapterNotificatorApi()
        return cls._instancia

    def build_send_notificacao(self, loja:Loja, id_usuario:int):
        try:
            notificacaoDict = {'id': None,
                               'mensagem': f"Loja com id {loja.id_} editada. \n{loja.__str__()}",
                               'from_user_id': id_usuario,
                               'to_loja_id': loja.id_}

            entidade: Notificacao = FabricaEntidades.criar(tipo='notificacao', dados=notificacaoDict)
            self.notificator.send(entidade)
            print('Notificacao enviada')
        except NotificationError as e:
            print('Erro ao enviar notificacao')

    def get_notificacoes(self, id_loja:int):
        return self.notificator.receive(id_loja)