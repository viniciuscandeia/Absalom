from abc import ABC, abstractmethod
from sqlite3 import Connection
from src.entidades.entidade_produto import Produto


class InterfaceEstrategiaProdutos(ABC):
    @abstractmethod
    def adicionar(self, produto: Produto):
        pass

    @abstractmethod
    def remover(self, id_: int):
        pass

    @abstractmethod
    def editar(self, id_: int, produto: Produto):
        pass

    @abstractmethod
    def verificar_existencia(self, id_: int):
        pass

    @abstractmethod
    def buscar(self, id_: int):
        pass

    @abstractmethod
    def listar(self, id_loja: int = None):
        pass

    @abstractmethod
    def gerar_novo_id(self):
        pass


class EstrategiaProdutosRAM(InterfaceEstrategiaProdutos):
    def __init__(self, repositorio: dict):
        self.repositorio = repositorio

    def adicionar(self, entidade: Produto):
        self.repositorio[entidade.id_] = entidade

    def remover(self, id_: int):
        del self.repositorio[id_]

    def editar(self, id_: int, produto: Produto):
        self.repositorio[id_] = produto

    def buscar(self, id_: int):
        return self.repositorio.get(id_, None)

    def verificar_existencia(self, id_: int) -> bool:
        return id_ in self.repositorio

    def listar(self, id_loja: int = None) -> dict:
        informacoes: dict = {}
        for produto in self.repositorio.values():
            if id_loja is None or produto.id_loja == id_loja:
                informacoes[produto.id_] = produto
        return informacoes

    def gerar_novo_id(self) -> int:
        if len(self.repositorio) == 0:
            return 1
        ultimo_id = max(self.repositorio.keys())
        return ultimo_id + 1


class EstrategiaProdutosDB(InterfaceEstrategiaProdutos):
    def __init__(self, repositorio_db: Connection):
        self.repositorio_db = repositorio_db

    def adicionar(self, entidade: Produto):
        cursor = self.repositorio_db.cursor()
        query = """
                INSERT INTO produtos (
                nome,
                descricao,
                preco,
                quantidade,
                id_loja)
                VALUES (?, ?, ?, ?, ?)
            """
        cursor.execute(
            query,
            (
                entidade.nome,
                entidade.descricao,
                entidade.preco,
                entidade.quantidade,
                entidade.id_loja,
            ),
        )
        self.repositorio_db.commit()

    def remover(self, id_: int):
        if self.verificar_existencia(id_):
            cursor = self.repositorio_db.cursor()
            query = "DELETE FROM produtos WHERE id = ?"
            cursor.execute(query, (id_,))
            self.repositorio_db.commit()
        else:
            raise ValueError("Produto não encontrado")

    def buscar(self, id_: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, nome, descricao, preco, quantidade, id_loja FROM produtos WHERE id = ?"
        cursor.execute(query, (id_,))
        resultado = cursor.fetchone()
        return Produto(
            id_=resultado[0],
            nome=resultado[1],
            descricao=resultado[2],
            preco=resultado[3],
            quantidade=resultado[4],
            id_loja=resultado[5],
        )

    def editar(self, id_: int, entidade: Produto):
        cursor = self.repositorio_db.cursor()
        query = """
            UPDATE produtos
            SET nome = ?,
            descricao = ?,
            preco = ?,
            quantidade = ?,
            id_loja = ?
            WHERE id = ?
        """
        cursor.execute(
            query,
            (
                entidade.nome,
                entidade.descricao,
                entidade.preco,
                entidade.quantidade,
                entidade.id_loja,
                id_,
            ),
        )
        self.repositorio_db.commit()

    def verificar_existencia(self, id_: int) -> bool:
        cursor = self.repositorio_db.cursor()
        query = "SELECT 1 FROM produtos WHERE id = ?"
        cursor.execute(query, (id_,))
        return cursor.fetchone() is not None

    def listar(self, id_loja: int) -> dict:
        informacoes: dict = {}
        cursor = self.repositorio_db.cursor()

        query = "SELECT id, nome, descricao, preco, quantidade, id_loja FROM produtos WHERE 1=1"
        parametros = []

        if id_loja is not None:
            query += " AND id_loja = ?"
            parametros.append(id_loja)

        cursor.execute(query, parametros)
        resultados = cursor.fetchall()

        # Iterar sobre os resultados e criar objetos Produto
        for resultado in resultados:
            produto = Produto(
                id_=resultado[0],
                nome=resultado[1],
                descricao=resultado[2],
                preco=resultado[3],
                quantidade=resultado[4],
                id_loja=resultado[5],
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
