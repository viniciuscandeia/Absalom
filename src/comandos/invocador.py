from .comando import Comando


class Invocador:
    def __init__(self):
        pass

    @classmethod
    def executar_comando(self, comando: Comando):
        return comando.execute()
