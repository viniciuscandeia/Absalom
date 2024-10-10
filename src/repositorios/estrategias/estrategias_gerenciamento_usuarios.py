# Deverão existir 3 estratégias:
# 1. Estratégia para lidar com usuários na RAM
# 2. Estratégia para lidar com administradores no BD
# 3. Estratégia para lidar com usuários no BD


# import sqlite3
from abc import ABC, abstractmethod
from ...entidades.entidades_usuarios import Usuario

# # Criar método de procurar.

class GerenciamentoEstrategia(ABC):
    @abstractmethod
    def adicionar(self, id_: int, usuario: Usuario):
        pass

    @abstractmethod
    def remover(self, id_: int):
        pass

    @abstractmethod
    def editar(self, id_: int, usuario: Usuario):
        pass

    @abstractmethod
    def buscar(self, id_: int):
        pass

    @abstractmethod
    def _existe(self, id_: int):
        pass

    @abstractmethod
    def listar(self, tipo: str, id_loja: int):
        pass


class GerenciamentoUsuariosRAM(GerenciamentoEstrategia):
    def __init__(self, repositorio: dict):
        self.repositorio: dict = repositorio

    def adicionar(self, id_: int, usuario: Usuario):
        if not self._existe(id_):
            self.repositorio[id_] = usuario
        else:
            raise ValueError("Usuário já existe")

    def remover(self, id_: int):
        if self._existe(id_):
            del self.repositorio[id_]
        else:
            raise ValueError("Usuário não encontrado")

    def editar(self, id_: int, usuario: Usuario):
        if self._existe(id_):
            self.repositorio[id_] = usuario
        else:
            raise ValueError("Usuário não encontrado")

    def buscar(self, id_: int):
        return self.repositorio.get(id_, None)

    def _existe(self, id_: int) -> bool:
        return id_ in self.repositorio

    def listar(self, tipo: str = None, id_loja: int = None) -> list[Usuario]:
        lista: list[Usuario] = []
        for usuario in self.repositorio.values():
            if (tipo is None or usuario.tipo == tipo) and (id_loja is None or usuario.id_loja == id_loja):
                lista.append(usuario)
        return lista


class GerenciamentoUsuariosDB(GerenciamentoEstrategia):
    def __init__(self, repositorio_db):
        self.repositorio_db = repositorio_db

    def adicionar(self, id_: int, usuario: Usuario):
        if not self._existe(id_):
            cursor = self.repositorio_db.cursor()
            query = """
                INSERT INTO usuarios (id, nome, username, email, senha, tipo, id_loja)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (id_, usuario.nome, usuario.username,
                           usuario.email, usuario.senha, usuario.tipo, usuario.id_loja))
            self.repositorio_db.commit()
        else:
            raise ValueError("Usuário já existe")

    def remover(self, id_: int):
        if self._existe(id_):
            cursor = self.repositorio_db.cursor()
            query = "DELETE FROM usuarios WHERE id = ?"
            cursor.execute(query, (id_,))
            self.repositorio_db.commit()
        else:
            raise ValueError("Usuário não encontrado")

    def buscar(self, id_: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, nome, username, email, senha, tipo, id_loja FROM usuarios WHERE id = ?"
        cursor.execute(query, (id_,))
        resultado = cursor.fetchone()
        if resultado:
            return Usuario(
                id_=resultado[0], nome=resultado[1], username=resultado[2],
                email=resultado[3], senha=resultado[4], tipo=resultado[5], id_loja=resultado[6]
            )
        else:
            return None

    def editar(self, id_: int, usuario: Usuario):
        if self._existe(id_):
            cursor = self.repositorio_db.cursor()
            query = """
                UPDATE usuarios
                SET nome = ?, username = ?, email = ?, senha = ?, id_loja = ?
                WHERE id = ?
            """
            cursor.execute(query, (usuario.nome, usuario.username,
                           usuario.email, usuario.senha, usuario.id_loja, id_))
            self.repositorio_db.commit()
        else:
            raise ValueError("Usuário não encontrado")

    def _existe(self, id_: int) -> bool:
        cursor = self.repositorio_db.cursor()
        query = "SELECT 1 FROM usuarios WHERE id = ?"
        cursor.execute(query, (id_,))
        return cursor.fetchone() is not None


    def listar(self, tipo: str = None, id_loja: int = None) -> list[Usuario]:
        lista: list[Usuario] = []
        cursor = self.repositorio_db.cursor()

        # Construir a query dinamicamente com base nos parâmetros
        query = "SELECT id, nome, username, email, senha, tipo, id_loja FROM usuarios WHERE 1=1"
        parametros = []

        if tipo is not None:
            query += " AND tipo = ?"
            parametros.append(tipo)

        if id_loja is not None:
            query += " AND id_loja = ?"
            parametros.append(id_loja)

        cursor.execute(query, parametros)
        resultados = cursor.fetchall()

        # Iterar sobre os resultados e criar objetos Usuario
        for resultado in resultados:
            usuario = Usuario(
                id_=resultado[0], nome=resultado[1], username=resultado[2],
                email=resultado[3], senha=resultado[4], tipo=resultado[5], id_loja=resultado[6]
            )
            lista.append(usuario)

        return lista
