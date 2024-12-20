from src.entidades.entidade_notificacao import Notificacao
from ..estrategias.estrategias_notificacoes import InterfaceEstrategiaNotificacao


class GerenciadorNotificacoes:
    def __init__(self, estrategia: InterfaceEstrategiaNotificacao):
        self.estrategia = estrategia

    def send(self, notificacao: Notificacao):
        self.estrategia.send(notificacao)

    def receive(self, id_loja: int):
        return self.estrategia.receive(id_loja)

