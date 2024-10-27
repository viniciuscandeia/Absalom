import sqlite3

CAMINHO_DB: str = 'src/repositorios/database.db'


class RepositorioVendasRAM:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._repositorio = {}
        return cls._instancia

    def pegar_repositorio(self):
        return self._repositorio

class RepositorioVendasDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._conexao_db = cls._criar_conexao(cls)
        return cls._instancia

    def _criar_conexao(self):
        conexao = sqlite3.connect(CAMINHO_DB)
        return conexao

    def pegar_repositorio(self):
        return self._conexao_db
