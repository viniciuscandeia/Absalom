from src.entidades.entidade_produto import Produto
from src.repositorios.estrategias.gerenciamento_estrategia import GerenciamentoEstrategia
from sqlite3 import Connection

class GerenciamentoProdutoRAM(GerenciamentoEstrategia[Produto]):
    def __init__(self, repositorio: dict):
        self.repositorio = repositorio

    def adicionar(self, entidade: Produto):
        produtos: list[Produto] = self.listar()
        id: int
        if len(produtos) == 0:
            id = 0

        if len(produtos) > 0:
            id = produtos[len(produtos) - 1].id_ + 1

        entidade.id_ = id
        self.repositorio[id] = entidade

    def remover(self, id_: int):
        if self._existe(id_):
            del self.repositorio[id_]
        else:
            raise ValueError("Produto não encontrado")

    def editar(self, id_: int, loja: Produto):
        if self._existe(id_):
            self.repositorio[id_] = loja
        else:
            raise ValueError("Produto não encontrado")

    def buscar(self, id_: int):
        return self.repositorio.get(id_, None)

    def _existe(self, id_: int) -> bool:
        return id_ in self.repositorio

    def listar(self) -> list[Produto]:
        lista: list[Produto] = []
        for loja in self.repositorio.values():
            lista.append(loja)
        return lista



class GerenciamentoProdutoDB(GerenciamentoEstrategia[Produto]):
    def __init__(self, repositorio_db: Connection):
        self.repositorio_db = repositorio_db

    def adicionar(self, entidade: Produto):
            cursor = self.repositorio_db.cursor()
            query = """
                INSERT INTO produto (
                nome, 
                tipo, 
                preco, 
                quantidade, 
                id_loja)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (entidade.nome,
                                   entidade.tipo,
                                   entidade.preco,
                                   entidade.quantidade,
                                   entidade.id_loja))
            self.repositorio_db.commit()

    def remover(self, id_: int):
        if self._existe(id_):
            cursor = self.repositorio_db.cursor()
            query = "DELETE FROM produto WHERE id = ?"
            cursor.execute(query, (id_,))
            self.repositorio_db.commit()
        else:
            raise ValueError("Produto não encontrado")

    def buscar(self, id_: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, nome, tipo, preco, quantidade, id_loja FROM produto WHERE id = ?"
        cursor.execute(query, (id_,))
        resultado = cursor.fetchone()
        if resultado:
            return Produto(
                id_ = resultado[0],
                nome = resultado[1],
                tipo = resultado[2],
                preco = resultado[3],
                quantidade = resultado[4],
                id_loja = resultado[5],
            )
        else:
            raise ValueError("Erro ao buscar produto")


    def editar(self, id_: int, entidade: Produto):
        if self._existe(id_):
            cursor = self.repositorio_db.cursor()
            query = """
                UPDATE produto
                SET nome = ?, 
                tipo = ?, 
                preco = ?, 
                quantidade = ?, 
                id_loja = ?
                WHERE id = ?
            """
            cursor.execute(query, (entidade.nome,
                                   entidade.tipo,
                                   entidade.preco,
                                   entidade.quantidade,
                                   entidade.id_loja,
                                   id_))

            self.repositorio_db.commit()
        else:
            raise ValueError("Produto não encontrado")

    def _existe(self, id_: int) -> bool:
            cursor = self.repositorio_db.cursor()
            query = "SELECT 1 FROM produto WHERE id = ?"
            cursor.execute(query, (id_,))
            return cursor.fetchone() is not None

    def listar(self) -> list[Produto]:
        lista: list[Produto] = []
        cursor = self.repositorio_db.cursor()

        query = "SELECT id, nome, tipo, preco, quantidade, id_loja FROM produto"

        cursor.execute(query)
        for resultado in cursor.fetchall():
            usuario = Produto(
                id_=resultado[0],
                nome=resultado[1],
                tipo=resultado[2],
                preco=resultado[3],
                quantidade=resultado[4],
                id_loja=resultado[5]
            )
            lista.append(usuario)

        return lista