from ..repositorios.gerenciadores.gerenciador_usuarios import GerenciadorUsuarios
from ..entidades.entidades_usuarios import Usuario

class AutenticacaoUsuario:
    _instancia = None

    def __new__(cls, gerenciador: GerenciadorUsuarios):
        if cls._instancia is None:
            cls._instancia = super(AutenticacaoUsuario, cls).__new__(cls)
            cls._instancia._gerenciador: GerenciadorUsuarios = gerenciador
            cls._instancia._usuario_autenticado = None
        return cls._instancia

    def autenticar(self, username, senha):
        # Faz a consulta no repositório
        usuario: Usuario = self._gerenciador.validar(username, senha)
        if usuario:
            self._usuario_autenticado = usuario
            return True
        self._usuario_autenticado = None
        return False

    def usuario_autenticado(self):
        return self._usuario_autenticado
