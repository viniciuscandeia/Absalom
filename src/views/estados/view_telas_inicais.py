from .view_estado_tela import EstadoTela


class TelaInicialAdministrador(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = \
            """
        --- Tela Inicial ---
        1 - Gerenciar Usuários
        2 - Logout
        """
        print(mensagem)
        opcao = input('Opção: ')
        return opcao

    def proxima_tela(self, opcao):
        from .view_gerenciar_usuarios import TelaGerenciarUsuarios

        self.transicoes = {
            'gerenciar_usuarios': TelaGerenciarUsuarios(),
        }

        self.atualizar_estado(opcao, self.transicoes)

    def tela_anterior(self, opcao: str):
        from .view_login import TelaLogin

        self.transicoes = {
            'logout': TelaLogin(),
        }

        self.atualizar_estado(opcao, self.transicoes)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaInicialGerente(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = \
            """
        --- Tela Inicial ---
        1 - Gerenciar Usuários
        2 - Gerenciar Produtos
        3 - Realizar Venda
        4 - Logout
        """

        print(mensagem)
        opcao = input('Opção: ')
        return opcao

    def proxima_tela(self, opcao):
        from .view_gerenciar_usuarios import TelaGerenciarUsuarios

        self.transicoes = {
            'gerenciar_usuarios': TelaGerenciarUsuarios(),
            'gerenciar_produtos': None,
            'realizar_venda': None,
        }

        self.atualizar_estado(opcao, self.transicoes)

    def tela_anterior(self, opcao: str):
        from .view_login import TelaLogin

        self.transicoes = {
            'logout': TelaLogin(),
        }

        self.atualizar_estado(opcao, self.transicoes)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaInicialVendedor(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = \
            """
        --- Tela Inicial ---
        1 - Realizar Venda
        2 - Logout
        """

        print(mensagem)
        opcao = input('Opção: ')
        return opcao

    def proxima_tela(self, opcao):

        self.transicoes = {
            'realizar_venda': None,
        }

        self.atualizar_estado(opcao, self.transicoes)

    def tela_anterior(self, opcao: str):
        from .view_login import TelaLogin

        self.transicoes = {
            'logout': TelaLogin(),
        }

        self.atualizar_estado(opcao, self.transicoes)


    def preparar_dados_recebidos(self, dados: list):
        pass

