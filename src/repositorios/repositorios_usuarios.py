import sqlite3

CAMINHO_USUARIOS_DB: str = 'src/repositorios/usuarios.db'


class RepositorioUsuariosRAM:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._repositorio = {}
        return cls._instancia

    def pegar_repositorio(self):
        return self._repositorio


class RepositorioUsuariosDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._conexao_db = cls._criar_conexao()
        return cls._instancia

    @staticmethod
    def _criar_conexao():
        # Conecta ao banco de dados SQLite, por exemplo
        conexao = sqlite3.connect(CAMINHO_USUARIOS_DB)
        return conexao

    def pegar_repositorio(self):
        # Retorna a conexão ao invés de carregar os dados
        return self._conexao_db
