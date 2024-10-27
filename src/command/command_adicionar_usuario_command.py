from src.command.command import Command


class AdicionarUsuarioCommand(Command):
    def __init__(self, gerenciador_usuarios, usuario):
        self.gerenciador_usuarios = gerenciador_usuarios
        self.usuario = usuario

    def execute(self):
        self.gerenciador_usuarios.adicionar(self.usuario)
