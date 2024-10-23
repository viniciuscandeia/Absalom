# Deverão existir 3 estratégias:
# 1. Estratégia para lidar com usuários na RAM
# 2. Estratégia para lidar com administradores no BD
# 3. Estratégia para lidar com usuários no BD

from abc import ABC, abstractmethod
from sqlite3 import Connection

from ...entidades.entidades_usuarios import Usuario

# # Criar método de procurar.


class InterfaceEstrategiaUsuarios(ABC):
    @abstractmethod
    def adicionar(self, usuario: Usuario):
        pass

    @abstractmethod
    def remover(self, id_: int):
        pass

    @abstractmethod
    def editar(self, id_: int, usuario: Usuario):
        pass

    @abstractmethod
    def verificar_existencia(self, id_: int):
        pass

    @abstractmethod
    def buscar(self, id_: int):
        pass

    @abstractmethod
    def listar(self, tipo: str = None, id_loja: int = None):
        pass

    @abstractmethod
    def validar(self, username: str, senha: str):
        pass

    @abstractmethod
    def gerar_novo_id(self):
        pass


class EstrategiaUsuariosRAM(InterfaceEstrategiaUsuarios):
    def __init__(self, repositorio: dict):
        self.repositorio: dict = repositorio

    def adicionar(self, usuario: Usuario):
        self.repositorio[usuario.id_] = usuario

    def remover(self, id_: int):
        del self.repositorio[id_]

    def editar(self, id_: int, usuario: Usuario):
        self.repositorio[id_] = usuario

    def buscar(self, id_: int):
        return self.repositorio.get(id_)

    def verificar_existencia(self, id_: int) -> bool:
        return id_ in self.repositorio

    def listar(self, tipo: str = None, id_loja: int = None) -> list[Usuario]:
        lista: list[Usuario] = []
        for usuario in self.repositorio.values():
            if (tipo is None or usuario.tipo == tipo) and (
                id_loja is None or usuario.id_loja == id_loja
            ):
                lista.append(usuario)
        return lista

    def validar(self, username: str, senha: str):
        for usuario in self.repositorio.values():
            if usuario.username == username and usuario.senha == senha:
                return usuario
        return None

    def gerar_novo_id(self) -> int:
        if len(self.repositorio) == 0:
            return 1
        ultimo_id = max(self.repositorio.keys())
        return ultimo_id + 1


class EstrategiaUsuariosDB(InterfaceEstrategiaUsuarios):
    def __init__(self, repositorio_db: Connection):
        self.repositorio_db = repositorio_db

    def adicionar(self, usuario: Usuario):
        cursor = self.repositorio_db.cursor()
        query = """
                INSERT INTO usuarios (nome, username, email, senha, tipo, id_loja)
                VALUES (?, ?, ?, ?, ?, ?)
            """
        cursor.execute(
            query,
            (
                usuario.nome,
                usuario.username,
                usuario.email,
                usuario.senha,
                usuario.tipo,
                usuario.id_loja,
            ),
        )
        self.repositorio_db.commit()

    def remover(self, id_: int):
        cursor = self.repositorio_db.cursor()
        query = "DELETE FROM usuarios WHERE id = ?"
        cursor.execute(query, (id_,))
        self.repositorio_db.commit()

    def buscar(self, id_: int):
        cursor = self.repositorio_db.cursor()
        query = "SELECT id, nome, username, email, senha, tipo, id_loja FROM usuarios WHERE id = ?"
        cursor.execute(query, (id_,))
        resultado = cursor.fetchone()
        return Usuario(
            id_=resultado[0],
            nome=resultado[1],
            username=resultado[2],
            email=resultado[3],
            senha=resultado[4],
            tipo=resultado[5],
            id_loja=resultado[6],
        )

    def editar(self, id_: int, usuario: Usuario):
        cursor = self.repositorio_db.cursor()
        query = """
            UPDATE usuarios
            SET nome = ?, username = ?, email = ?, senha = ?, id_loja = ?
            WHERE id = ?
        """
        cursor.execute(
            query,
            (
                usuario.nome,
                usuario.username,
                usuario.email,
                usuario.senha,
                usuario.id_loja,
                id_,
            ),
        )
        self.repositorio_db.commit()

    def verificar_existencia(self, id_: int) -> bool:
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
                id_=resultado[0],
                nome=resultado[1],
                username=resultado[2],
                email=resultado[3],
                senha=resultado[4],
                tipo=resultado[5],
                id_loja=resultado[6],
            )
            lista.append(usuario)

        return lista

    def validar(self, username: str, senha: str):
        cursor = self.repositorio_db.cursor()

        # Executa a consulta SQL para verificar o usuário
        cursor.execute(
            """
            SELECT id, nome, username, email, senha, tipo, id_loja
            FROM usuarios
            WHERE username = ? AND senha = ?
        """,
            (username, senha),
        )

        # Recupera o resultado da consulta
        resultado = cursor.fetchone()

        if resultado:
            # Cria uma instância de Usuario com os dados retornados
            usuario = Usuario(
                id_=resultado[0],
                nome=resultado[1],
                username=resultado[2],
                email=resultado[3],
                senha=resultado[4],
                tipo=resultado[5],
                id_loja=resultado[6],
            )
            return usuario
        return None

    def gerar_novo_id(self) -> int:
        cursor = self.repositorio_db.cursor()
        cursor.execute("SELECT MAX(id) FROM usuarios")
        resultado = cursor.fetchone()
        if resultado[0] is None:
            return 1
        return resultado[0] + 1
