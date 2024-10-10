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
            'erro': TelaLogin()
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)


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

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)
