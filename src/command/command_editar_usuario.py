from src.command.command import Command

class EditarUsuarioCommand(Command):
    def __init__(self, gerenciador_usuarios, id_usuario, usuario):
        self.gerenciador_usuarios = gerenciador_usuarios
        self.id_usuario = id_usuario
        self.usuario = usuario

    def execute(self):
        self.gerenciador_usuarios.editar(self.id_usuario, self.usuario)