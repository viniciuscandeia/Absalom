import uuid
from copy import deepcopy

from src.entidades.entidade_notificacao import Notificacao
from sqlite3 import Connection
from src.repositorios.estrategias.interface_estrategia_notificacao import InterfaceEstrategiaNotificacao


class EstrategiaNotificacoesFirebase(InterfaceEstrategiaNotificacao):
    def __init__(self, repositorio: list[Notificacao]):
        self.repositorio = repositorio

    def send(self, entidade: Notificacao):
        ultimo_id = 0

        if len(self.repositorio) > 0:
            ultimo_id = len(self.repositorio)

        entidade.id_ = ultimo_id
        entidade_copy = deepcopy(entidade)
        self.repositorio.append(entidade_copy)

    def receive(self, id_loja:int):
        filteredItems = []
        for notificacao in self.repositorio:
            if notificacao.to_loja_id == id_loja:
                filteredItems.append(notificacao)

        return filteredItems


class EstrategiaNotificacoesDB(InterfaceEstrategiaNotificacao):
    def __init__(self, repositorio_db: Connection):
        self.repositorio_db = repositorio_db

    def send(self, notificacao: Notificacao):
        cursor = self.repositorio_db.cursor()
        query = """
                INSERT INTO notificacoes (from_user_id, to_loja_id, mensagem)
                VALUES (?, ?, ?)
            """
        cursor.execute(query, (notificacao.from_user_id, notificacao.to_loja_id, notificacao.mensagem))
        self.repositorio_db.commit()

    def receive(self, id_loja:int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, mensagem, from_user_id, to_loja_id FROM notificacoes WHERE to_loja_id = ?"
        cursor.execute(query, (id_loja,))
        notificacoes = []

        for resultado in cursor.fetchall():
            notificacao =  Notificacao(
                id_=resultado[0],
                mensagem=resultado[1],
                from_user_id=resultado[2],
                to_loja_id=resultado[3]
            )
            notificacoes.append(notificacao)

        return notificacoes
