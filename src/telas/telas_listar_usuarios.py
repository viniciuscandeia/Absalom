from ..entidades.entidades_usuarios import Usuario
from .template_tela import TemplateTela

# O "_Administrador" indica que é uma tela para o Administrador


class TelaListar_Administrador(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Listar Administradores \n2 - Filtrar por Loja \n3 - Voltar \n"
        )
        print(mensagem)


class TelaListar_Gerente(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Listar Usuários \n2 - Voltar \n"
        print(mensagem)


class TelaListarAdministradores(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar Administradores --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        for item in informacoes:
            print(informacoes[item])

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Visualizar Administrador \n2 - Voltar \n"
        print(mensagem)


class TelaListarUsuarios(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar Usuários --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        for item in informacoes:
            print(informacoes[item])

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Visualizar Usuário \n2 - Voltar \n"
        print(mensagem)


class TelaPesquisarUsuario(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Pesquisar Usuário --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id": cls._coletar_entrada("ID: ")}


class TelaVisualizarUsuario(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Visualizar Usuário --- \n")

    @classmethod
    def _listar_informacoes(cls, usuario: Usuario):
        mensagem: str = (
            f"ID: {usuario.id_} \nNome: {usuario.nome} \nUsername: {usuario.username} \nEmail: {usuario.email} \nTipo: {usuario.tipo} \n"
        )
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Editar Usuário \n2 - Excluir Usuário \n3 - Voltar"
        print(mensagem)
