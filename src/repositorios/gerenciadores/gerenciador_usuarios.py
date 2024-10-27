from ...entidades.entidades_usuarios import Usuario
from ..estrategias.estrategias_usuarios import InterfaceEstrategiaUsuarios

# Esta classe irá receber uma estratégia para lidar com o repositório dos usuários.
# Pode receber duas estratégias:
#   1 - Repositório em RAM
#   2 - Repositório em BD


class GerenciadorUsuarios:
    def __init__(self, estrategia: InterfaceEstrategiaUsuarios):
        self.estrategia = estrategia

    def adicionar(self, entidade: Usuario):
        self.estrategia.adicionar(entidade)

    def remover(self, id_usuario: int):
        self.estrategia.remover(id_usuario)

    def editar(self, id_usuario: int, entidade: Usuario):
        self.estrategia.editar(id_usuario, entidade)

    def buscar(self, id_usuario: int):
        return self.estrategia.buscar(id_usuario)

    def verificar_existencia(self, id_usuario: int) -> bool:
        return self.estrategia.verificar_existencia(id_usuario)

    def listar(self, tipo: str = None, id_loja: int = None) -> dict:
        return self.estrategia.listar(tipo, id_loja)

    def validar(self, username: str, senha: str) -> Usuario:
        return self.estrategia.validar(username, senha)

    def gerar_novo_id(self) -> int:
        return self.estrategia.gerar_novo_id()
