from abc import ABC, abstractmethod
from sqlite3 import Connection

from src.entidades.entidade_venda import Venda


class InterfaceEstrategiaVendas(ABC):
    @abstractmethod
    def adicionar(self, venda: Venda):
        pass

    @abstractmethod
    def remover(self, id_venda: int):
        pass

    @abstractmethod
    def buscar(self, id_venda: int):
        pass

    @abstractmethod
    def listar(self, id_loja: int = None):
        pass

    @abstractmethod
    def gerar_novo_id(self):
        pass


class EstrategiaVendasRAM(InterfaceEstrategiaVendas):
    def __init__(self, repositorio: dict):
        self.repositorio = repositorio

    def adicionar(self, venda: Venda):
        self.repositorio[venda.id_venda] = venda

    def remover(self, id_venda: int):
        del self.repositorio[id_venda]

    def buscar(self, id_venda: int):
        return self.repositorio.get(id_venda, None)

    def listar(self, id_loja: int = None) -> dict:
        informacoes: dict = {}
        for venda in self.repositorio.values():
            if id_loja is None or venda.id_loja == id_loja:
                informacoes[venda.id_venda] = venda
        return informacoes

    def gerar_novo_id(self) -> int:
        if len(self.repositorio) == 0:
            return 1
        ultimo_id = max(self.repositorio.keys())
        return ultimo_id + 1


class EstrategiaVendasDB(InterfaceEstrategiaVendas):
    def __init__(self, repositorio_db: Connection):
        self.repositorio_db = repositorio_db

    # venda
    # loja

    def adicionar(self, entidade: Venda):
        cursor = self.repositorio_db.cursor()
        query = """
                INSERT INTO vendas (
                id_loja,
                id_vendedor,
                id_produto,
                quantidade,
                preco_total)
                VALUES (?, ?, ?, ?, ?)
            """
        cursor.execute(
            query,
            (
                entidade.id_loja,
                entidade.id_vendedor,
                entidade.id_produto,
                entidade.quantidade,
                entidade.preco_total,
            ),
        )
        self.repositorio_db.commit()

    def remover(self, id_venda: int):
        cursor = self.repositorio_db.cursor()
        query = "DELETE FROM vendas WHERE id = ?"
        cursor.execute(query, (id_venda,))
        self.repositorio_db.commit()

    def buscar(self, id_venda: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, id_loja, id_vendedor, id_produto, quantidade, preco_total FROM vendas WHERE id = ?"
        cursor.execute(query, (id_venda,))
        resultado = cursor.fetchone()
        return Venda(
            id_=resultado[0],
            id_loja=resultado[1],
            id_vendedor=resultado[2],
            id_produto=resultado[3],
            quantidade=resultado[4],
            preco_total=resultado[5],
        )

    def listar(self, id_loja: int) -> dict:
        informacoes: dict = {}
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, id_loja, id_vendedor, id_produto, quantidade, preco_total FROM vendas WHERE 1=1"
        parametros = []
        if id_loja is not None:
            query += " AND id_loja = ?"
            parametros.append(id_loja)
        cursor.execute(query, parametros)
        resultados = cursor.fetchall()
        # Iterar sobre os resultados e criar objetos Produto
        for resultado in resultados:
            produto = Venda(
                id_=resultado[0],
                id_loja=resultado[1],
                id_vendedor=resultado[2],
                id_produto=resultado[3],
                quantidade=resultado[4],
                preco_total=resultado[5],
            )
            informacoes[produto.id_] = produto
        return informacoes

    def gerar_novo_id(self) -> int:
        cursor = self.repositorio_db.cursor()
        cursor.execute("SELECT MAX(id) FROM produtos")
        resultado = cursor.fetchone()
        if resultado[0] is None:
            return 1
        return resultado[0] + 1
