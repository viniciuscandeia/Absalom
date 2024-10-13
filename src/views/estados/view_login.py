from .view_estado_tela import EstadoTela


class TelaLogin(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Login ---
        """
        print(mensagem)
        username = input('Username: ')
        senha = input('Senha: ')
        return {'username': username, 'senha': senha}

    def proxima_tela(self, opcao):
        # Importações dentro do método para evitar importação circular
        from .view_telas_inicais import TelaInicialAdministrador, TelaInicialGerente, TelaInicialVendedor

        self.transicoes = {
            'administrador': TelaInicialAdministrador(),
            'gerente': TelaInicialGerente(),
            'vendedor': TelaInicialVendedor(),
            'erro': TelaLoginErro()
        }

        self.atualizar_estado(opcao, self.transicoes)

    def tela_anterior(self, opcao: str):
        pass

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaLoginErro(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Erro ao realizar login! Username/senha inválido(s). ---
        """
        print(mensagem)

    def proxima_tela(self, opcao):
        self.transicoes = {
            'login': TelaLogin()
        }

        self.atualizar_estado(opcao, self.transicoes)

    def tela_anterior(self, opcao: str):
        pass

    def preparar_dados_recebidos(self, dados: list):
        pass
