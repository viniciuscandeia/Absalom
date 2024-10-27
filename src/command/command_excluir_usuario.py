from src.command.command import Command


class ExcluirUsuarioCommand(Command):
    def __init__(self, gerenciador_usuarios, id_usuario):
        self.gerenciador_usuarios = gerenciador_usuarios
        self.id_usuario = id_usuario

    def execute(self):
        self.gerenciador_usuarios.remover(self.id_usuario)
