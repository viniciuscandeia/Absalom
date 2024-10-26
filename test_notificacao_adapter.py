import uuid

from src.adapter.NotificatorApi import NotificatorApi
from src.adapter.notification.DatabaseAdapterNotificatorApi import DatabaseAdapterNotificatorApi
from src.adapter.notification.FirebaseAdapterNotificatorApi import FirebaseAdapterNotificatorApi
from src.entidades.entidade_notificacao import Notificacao
from src.fabricas.fabrica_entidades import FabricaEntidades

if __name__ == '__main__':
    dict = {}
    dict['id'] = None
    dict['mensagem'] = "Notificacao"
    dict['from_user_id'] = 1
    dict['to_loja_id'] = 3
    entidade = FabricaEntidades.criar_entidade(tipo='notificacao', dados=dict)

    class TestClient:
        def __init__(self, notificator: NotificatorApi):
            self.notificator = notificator

        def doSomething(self):
            # ...
            notificacao: Notificacao = entidade;
            self.notificator.send(notificacao)

        def receive(self, id_loja:int):
            # ...
            return self.notificator.receive(id_loja)
    testClient =    TestClient(FirebaseAdapterNotificatorApi())

    testClient.doSomething()
    testClient.doSomething()
    testClient.doSomething()

    for notificacao in testClient.receive(3):
        print(notificacao)

