from tokenize import String
from uuid import uuid4

from src.repositorios.estrategias.gerenciamento_estrategia import GerenciamentoEstrategia
from src.entidades.entidade_loja import Loja
from sqlite3 import Connection

class GerenciamentoLojaRAM(GerenciamentoEstrategia[Loja]):
    def __init__(self, repositorio: dict):
        self.repositorio = repositorio

    def adicionar(self, entidade: Loja):
        lojas: list[Loja] = self.listar()
        id: int
        if len(lojas) == 0:
            id = 0

        if len(lojas) > 0:
            id = lojas[len(lojas) - 1].id_ + 1

        entidade.id_ = id
        self.repositorio[id] = entidade

    def remover(self, id_: int):
        if self._existe(id_):
            del self.repositorio[id_]
        else:
            raise ValueError("Loja não encontrado")

    def editar(self, id_: int, loja: Loja):
        if self._existe(id_):
            self.repositorio[id_] = loja
        else:
            raise ValueError("Loja não encontrado")

    def buscar(self, id_: int):
        return self.repositorio.get(id_, None)

    def _existe(self, id_: int) -> bool:
        return id_ in self.repositorio

    def listar(self) -> list[Loja]:
        lista: list[Loja] = []
        for loja in self.repositorio.values():
                lista.append(loja)
        return lista


class GerenciamentoLojaDB(GerenciamentoEstrategia[Loja]):
    def __init__(self, repositorio_db: Connection):
        self.repositorio_db = repositorio_db

    def adicionar(self, entidade: Loja):
            cursor = self.repositorio_db.cursor()
            query = """
                INSERT INTO loja (nome, endereco)
                VALUES (?, ?)
            """
            cursor.execute(query, (entidade.nome, entidade.endereco))
            self.repositorio_db.commit()

    def remover(self, id_: int):
        if self._existe(id_):
            cursor = self.repositorio_db.cursor()
            query = "DELETE FROM loja WHERE id = ?"
            cursor.execute(query, (id_,))
            self.repositorio_db.commit()
        else:
            raise ValueError("loja não encontrada")

    def buscar(self, id_: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, nome, endereco FROM loja WHERE id = ?"
        cursor.execute(query, (id_,))
        resultado = cursor.fetchone()
        if resultado:
            return Loja(
                id_=resultado[0], nome=resultado[1], endereco=resultado[2]
            )
        else:
            raise ValueError("Erro ao buscar loja")


    def editar(self, id_: int, loja: Loja):
        if self._existe(id_):
            cursor = self.repositorio_db.cursor()
            query = """
                UPDATE loja
                SET nome = ?, endereco = ?
                WHERE id = ?
            """
            cursor.execute(query, (loja.nome, loja.endereco, id_))
            self.repositorio_db.commit()
        else:
            raise ValueError("Usuário não encontrado")

    def _existe(self, id_: int) -> bool:
            cursor = self.repositorio_db.cursor()
            query = "SELECT 1 FROM loja WHERE id = ?"
            cursor.execute(query, (id_,))
            return cursor.fetchone() is not None

    def listar(self, tipo: str = None, id_loja: int = None) -> list[Loja]:
        lista: list[Loja] = []
        cursor = self.repositorio_db.cursor()

        # Construir a query dinamicamente com base nos parâmetros
        query = "SELECT id, nome, endereco FROM loja WHERE 1=1"

        cursor.execute(query)
        # Iterar sobre os resultados e criar objetos Usuario
        for resultado in cursor.fetchall():
            usuario = Loja(
                id_=resultado[0], nome=resultado[1], endereco=resultado[2])
            lista.append(usuario)

        return lista