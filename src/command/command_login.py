from src.command.command import Command

class CommandLogin(Command):
    def __init__(self, autenticador, username, senha):
        self.autenticador = autenticador
        self.username = username
        self.senha = senha

    def execute(self):
        # Lógica de autenticação
        self.autenticador.autenticar(self.username, self.senha)
        return self.autenticador.usuario_autenticado()  # Retorna o usuário autenticado
