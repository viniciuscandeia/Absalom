from src.command.command import Comando


class ExcluirUsuarioComando(Comando):
    def __init__(self, gerenciador_usuarios, id_usuario: int):
        self.gerenciador_usuarios = gerenciador_usuarios
        self.id_usuario: int = id_usuario

    def execute(self):
        self.gerenciador_usuarios.remover(self.id_usuario)
