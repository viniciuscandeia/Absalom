from .template_tela import TemplateTela

# O "_Administrador" indica que é uma tela para o Administrador


class TelaListar_Administrador(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Listar Administradores \n2 - Filtrar por Loja \n3 - Voltar \n"
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
        print("--- Listar Administradores --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        for item in informacoes:
            print(informacoes[item])

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Visualizar Administrador \n2 - Voltar \n"
        print(mensagem)


class TelaFiltrarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Filtrar por Loja --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Listar Lojas \n2 - Pesquisar Loja \n3 - Voltar \n"
        print(mensagem)


class TelaListarLojas(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar Lojas --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        for item in informacoes:
            print(informacoes[item])

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Visualizar Loja \n2 - Voltar \n"
        print(mensagem)
