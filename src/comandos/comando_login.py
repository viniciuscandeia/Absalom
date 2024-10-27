from .comando import Comando

class ComandoLogin(Comando):
    def __init__(self, autenticador, username: str, senha: str):
        self.autenticador = autenticador
        self.username: str = username
        self.senha: str = senha

    def execute(self):
        # Lógica de autenticação
        self.autenticador.autenticar(self.username, self.senha)
        return self.autenticador.usuario_autenticado()  # Retorna o usuário autenticado
