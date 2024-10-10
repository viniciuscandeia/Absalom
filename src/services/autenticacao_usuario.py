from ..repositorios.estrategias.gerenciador_repositorio_usuarios import GerenciadorRepositorioUsuarios
from ..entidades.entidades_usuarios import Usuario

class AutenticacaoUsuario:
    _instancia = None

    def __new__(cls, gerenciador: GerenciadorRepositorioUsuarios):
        if cls._instancia is None:
            cls._instancia = super(AutenticacaoUsuario, cls).__new__(cls)
            cls._instancia._gerenciador: GerenciadorRepositorioUsuarios = gerenciador
            cls._instancia._usuario_autenticado = None
        return cls._instancia

    def autenticar(self, username, senha):
        # Faz a consulta no repositório
        usuario: Usuario = self._gerenciador.validar(username, senha)
        if usuario:
            self._usuario_autenticado = usuario
            return True
        return False

    def usuario_autenticado(self):
        return self._usuario_autenticado
