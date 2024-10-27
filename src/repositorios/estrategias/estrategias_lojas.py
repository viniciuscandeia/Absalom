from src.entidades.entidade_loja import Loja
from sqlite3 import Connection
from abc import ABC, abstractmethod


class InterfaceEstrategiaLojas(ABC):
    @abstractmethod
    def adicionar(self, loja: Loja):
        pass

    @abstractmethod
    def remover(self, id_loja: int):
        pass

    @abstractmethod
    def editar(self, id_loja: int, loja: Loja):
        pass

    @abstractmethod
    def buscar(self, id_loja: int):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def gerar_novo_id(self):
        pass


class EstrategiaLojasRAM(InterfaceEstrategiaLojas):
    def __init__(self, repositorio: dict):
        self.repositorio = repositorio

    def adicionar(self, entidade: Loja):
        self.repositorio[entidade.id_] = entidade

    def remover(self, id_: int):
        del self.repositorio[id_]

    def editar(self, id_loja: int, entidade: Loja):
        self.repositorio[id_loja] = entidade

    def buscar(self, id_loja: int):
        return self.repositorio.get(id_loja)

    def listar(self) -> dict:
        informacoes: dict = {}
        for loja in self.repositorio.values():
            informacoes[loja.id_] = loja
        return informacoes

    def gerar_novo_id(self) -> int:
        if len(self.repositorio) == 0:
            return 1
        ultimo_id = max(self.repositorio.keys())
        return ultimo_id + 1


class EstrategiaLojasDB(InterfaceEstrategiaLojas):
    def __init__(self, repositorio_db: Connection):
        self.repositorio_db = repositorio_db

    def adicionar(self, entidade: Loja):
        cursor = self.repositorio_db.cursor()
        query = """
                INSERT INTO lojas (nome, endereco)
                VALUES (?, ?)
            """
        cursor.execute(query, (entidade.nome, entidade.endereco))
        self.repositorio_db.commit()

    def remover(self, id_loja: int):
        cursor = self.repositorio_db.cursor()
        query = "DELETE FROM lojas WHERE id = ?"
        cursor.execute(query, (id_loja,))
        self.repositorio_db.commit()

    def buscar(self, id_loja: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, nome, endereco FROM lojas WHERE id = ?"
        cursor.execute(query, (id_loja,))
        resultado = cursor.fetchone()
        return Loja(
            id_=resultado[0], nome=resultado[1], endereco=resultado[2]
        )

    def editar(self, id_loja: int, loja: Loja):
        cursor = self.repositorio_db.cursor()
        query = """
            UPDATE lojas
            SET nome = ?, endereco = ?
            WHERE id = ?
        """
        cursor.execute(query, (loja.nome, loja.endereco, id_loja))
        self.repositorio_db.commit()

    def listar(self) -> dict:
        informacoes: dict = {}
        cursor = self.repositorio_db.cursor()

        # Construir a query dinamicamente com base nos parâmetros
        query = "SELECT id, nome, endereco FROM lojas WHERE 1=1"

        cursor.execute(query)
        # Iterar sobre os resultados e criar objeto Loja
        for resultado in cursor.fetchall():
            loja = Loja(
                id_=resultado[0], nome=resultado[1], endereco=resultado[2])
            informacoes[loja.id_] = loja

        return informacoes

    def gerar_novo_id(self) -> int:
        cursor = self.repositorio_db.cursor()
        cursor.execute("SELECT MAX(id) FROM lojas")
        resultado = cursor.fetchone()
        if resultado[0] is None:
            return 1
        return resultado[0] + 1
