from src.repositorios.estrategias.gerenciamento_estrategia import InterfaceEstrategia
from src.entidades.entidade_loja import Loja
from sqlite3 import Connection


class EstrategiaLojasRAM(InterfaceEstrategia):
    def __init__(self, repositorio: dict):
        self.repositorio = repositorio

    def adicionar(self, entidade: Loja):
        self.repositorio[entidade.id_] = entidade

    def remover(self, id_: int):
        del self.repositorio[id_]

    def editar(self, id_: int, entidade: Loja):
        self.repositorio[id_] = entidade

    def buscar(self, id_: int):
        return self.repositorio.get(id_)

    def verificar_existencia(self, id_: int) -> bool:
        return id_ in self.repositorio

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



class EstrategiaLojaDB(InterfaceEstrategia):
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

    def remover(self, id_: int):
        if self.verificar_existencia(id_):
            cursor = self.repositorio_db.cursor()
            query = "DELETE FROM lojas WHERE id = ?"
            cursor.execute(query, (id_,))
            self.repositorio_db.commit()
        else:
            raise ValueError("Loja não encontrada")

    def buscar(self, id_: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, nome, endereco FROM lojas WHERE id = ?"
        cursor.execute(query, (id_,))
        resultado = cursor.fetchone()
        if resultado:
            return Loja(
                id_=resultado[0], nome=resultado[1], endereco=resultado[2]
            )
        else:
            raise ValueError("Erro ao buscar loja")

    def editar(self, id_: int, loja: Loja):
        if self.verificar_existencia(id_):
            cursor = self.repositorio_db.cursor()
            query = """
                UPDATE lojas
                SET nome = ?, endereco = ?
                WHERE id = ?
            """
            cursor.execute(query, (loja.nome, loja.endereco, id_))
            self.repositorio_db.commit()
        else:
            raise ValueError("Loja não encontrado")

    def verificar_existencia(self, id_: int) -> bool:
        cursor = self.repositorio_db.cursor()
        query = "SELECT 1 FROM lojas WHERE id = ?"
        cursor.execute(query, (id_,))
        return cursor.fetchone() is not None

    def listar(self, tipo: str = None, id_loja: int = None) -> dict:
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
