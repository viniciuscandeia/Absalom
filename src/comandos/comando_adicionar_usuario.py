from .comando import Comando


class AdicionarUsuarioComando(Comando):
    def __init__(self, gerenciador_usuarios, usuario):
        self.gerenciador_usuarios = gerenciador_usuarios
        self.usuario = usuario

    def execute(self):
        self.gerenciador_usuarios.adicionar(self.usuario)
