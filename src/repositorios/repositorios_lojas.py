import sqlite3

CAMINHO_USUARIOS_DB: str = 'src/repositorios/database.db'


class RepositorioLojasRAM:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._repositorio = {}
        return cls._instancia

    def pegar_repositorio(self):
        return self._repositorio

class RepositorioLojasDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._conexao_db = cls._criar_conexao()
        return cls._instancia

    def _criar_conexao(self):
        # Conecta ao banco de dados SQLite, por exemplo
        conexao = sqlite3.connect(CAMINHO_USUARIOS_DB)
        return conexao

    def pegar_repositorio(self):
        # Retorna a conexão ao invés de carregar os dados
        return self._conexao_db
