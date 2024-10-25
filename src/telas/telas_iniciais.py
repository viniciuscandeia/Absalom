from .template_tela import TemplateTela


class TelaInicialAdministrador(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Tela Inicial --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Gerenciar Usuários \n2 - Gerenciar Lojas \n3 - Logout \n"
        print(mensagem)

class TelaInicialGerente(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Tela Inicial --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Gerenciar Usuários \n2 - Gerenciar Produtos \n3 - Realizar Venda \n4 - Logout \n"
        )
        print(mensagem)


class TelaInicialVendedor(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Tela Inicial --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Realizar Venda \n2 - Logout \n"
        )
        print(mensagem)
