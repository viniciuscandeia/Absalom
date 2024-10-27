from .comando import Comando


class EditarUsuarioComando(Comando):
    def __init__(self, gerenciador_usuarios, id_usuario: int, usuario):
        self.gerenciador_usuarios = gerenciador_usuarios
        self.id_usuario: int = id_usuario
        self.usuario = usuario

    def execute(self):
        self.gerenciador_usuarios.editar(self.id_usuario, self.usuario)
