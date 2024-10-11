from .view_estado_tela import EstadoTela

# O "_Administrador" indica que é uma tela para o Administrador


class TelaListar_Administradores(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Listar ---
        1 - Listar Administradores
        2 - Filtrar por Loja
        3 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):
        from .view_gerenciar_usuarios import TelaGerenciarUsuarios

        self.transicoes = {
            "listar": None,
            "filtrar": None,
            "voltar": TelaGerenciarUsuarios(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)


class TelaListar_Gerente(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Listar ---
        1 - Listar Usuários
        3 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):
        from .view_gerenciar_usuarios import TelaGerenciarUsuarios

        self.transicoes = {
            "listar": None,
            "voltar": TelaGerenciarUsuarios(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)


# # Como receber a lista?


class TelaListarAdministradores(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Listar Administradores ---
        1 - Visualizar Administrador
        2 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):

        self.transicoes = {
            "visualizar": None,
            "voltar": TelaListar_Administradores(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)


class TelaFiltrarLoja(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Filtrar por Loja ---
        1 - Listar Lojas
        2 - Pesquisar Loja
        3 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):

        self.transicoes = {
            "listar": None,
            "pesquisar": None,
            "voltar": TelaListar_Administradores(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)


class TelaListarLojas(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = """
        --- Listar Lojas ---
        1 - Visualizar Loja
        2 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):

        self.transicoes = {
            "visualizar": None,
            "voltar": TelaFiltrarLoja(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)
