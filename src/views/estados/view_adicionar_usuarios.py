from .view_estado_tela import EstadoTela

# O "_Administrador" indica que é uma tela para o Administrador


class TelaAdicionarUsuarios_Administrador(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Escolha o tipo de usuário ---
        1 - Adicionar Administrador
        2 - Adicionar Gerente
        3 - Adicionar Vendedor
        4 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):
        from .view_gerenciar_usuarios import TelaGerenciarUsuarios

        self.transicoes = {
            "adicionar_administrador": TelaAdicionarAdministrador(),
            "adicionar_gerente": TelaAdicionarGerente(),
            "adicionar_vendedor": TelaAdicionarVendedor(),
            "voltar": TelaGerenciarUsuarios(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaAdicionarUsuarios_Gerente(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Escolha o tipo de usuário ---
        1 - Adicionar Gerente
        2 - Adicionar Vendedor
        3 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):
        from .view_gerenciar_usuarios import TelaGerenciarUsuarios

        self.transicoes = {
            "adicionar_gerente": TelaAdicionarGerente(),
            "adicionar_vendedor": TelaAdicionarVendedor(),
            "voltar": TelaGerenciarUsuarios(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


# # Tornar mais flexível isso


class TelaAdicionarAdministrador(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Adicionar Administrador ---
        """
        print(mensagem)
        nome = input("Nome: ")
        username = input("Username: ")
        email = input("Email: ")
        senha = input("Senha: ")
        return {"nome": nome, "username": username, "email": email, "senha": senha}

    def proxima_tela(self, opcao):

        self.transicoes = {
            "sucesso": TelaAdicionarSucesso(),
            "erro_username": TelaAdicionarErroUsername(),
            "erro_email": TelaAdicionarErroEmail(),
            "erro_senha": TelaAdicionarErroSenha(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaAdicionarGerente(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    @classmethod
    def exibir(self):
        mensagem: str = """
        --- Adicionar Gerente ---
        """
        print(mensagem)
        nome = input("Nome: ")
        username = input("Username: ")
        email = input("Email: ")
        senha = input("Senha: ")
        return {"nome": nome, "username": username, "email": email, "senha": senha}

    def proxima_tela(self, opcao):

        self.transicoes = {
            "sucesso": TelaAdicionarSucesso(),
            "erro_username": TelaAdicionarErroUsername(),
            "erro_email": TelaAdicionarErroEmail(),
            "erro_senha": TelaAdicionarErroSenha(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaAdicionarVendedor(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Adicionar Vendedor ---
        """
        print(mensagem)
        nome = input("Nome: ")
        username = input("Username: ")
        email = input("Email: ")
        senha = input("Senha: ")
        return {"nome": nome, "username": username, "email": email, "senha": senha}

    def proxima_tela(self, opcao):

        self.transicoes = {
            "sucesso": TelaAdicionarSucesso(),
            "erro_username": TelaAdicionarErroUsername(),
            "erro_email": TelaAdicionarErroEmail(),
            "erro_senha": TelaAdicionarErroSenha(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaAdicionarSucesso(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Usuário adicionado com sucesso! ---
        """
        print(mensagem)

    def proxima_tela(self, opcao):

        self.transicoes = {
            "voltar_administrador": TelaAdicionarUsuarios_Administrador(),
            "voltar_gerente": TelaAdicionarUsuarios_Gerente(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaAdicionarErroUsername(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Erro ao adicionar usuário! O 'username' digitado já foi cadastrado no sistema. ---
        """
        print(mensagem)

    def proxima_tela(self, opcao):

        self.transicoes = {
            "voltar_administrador": TelaAdicionarAdministrador(),
            "voltar_gerente": TelaAdicionarGerente(),
            "voltar_vendedor": TelaAdicionarVendedor(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaAdicionarErroEmail(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Erro ao adicionar usuário! O 'email' digitado já foi cadastrado no sistema. ---
        """
        print(mensagem)

    def proxima_tela(self, opcao):

        self.transicoes = {
            "voltar_administrador": TelaAdicionarAdministrador(),
            "voltar_gerente": TelaAdicionarGerente(),
            "voltar_vendedor": TelaAdicionarVendedor(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaAdicionarErroSenha(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Erro ao adicionar usuário! A 'senha' deve atender as condições. ---
        1 - Tamanho mínimo: 8 caracteres.
        2 - Tamanho máximo: 128 caracteres.
        3 - Deve conter, pelo menos, uma letra maiúscula.
        4 - Deve conter, pelo menos, uma letra minúscula.
        5 - Deve conter, pelo menos, um número.
        6 - Deve conter, pelo menos, um caractere especial.
        """
        print(mensagem)

    def proxima_tela(self, opcao):

        self.transicoes = {
            "voltar_administrador": TelaAdicionarAdministrador(),
            "voltar_gerente": TelaAdicionarGerente(),
            "voltar_vendedor": TelaAdicionarVendedor(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass
