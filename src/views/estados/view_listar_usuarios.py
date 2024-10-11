from ...entidades.entidades_usuarios import Usuario
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
            "listar": TelaListarAdministradores(),
            "filtrar": None,
            "voltar": TelaGerenciarUsuarios(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass


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

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaListarAdministradores(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}
        self.conteudo: str = ""

    def exibir(self):
        mensagem: str = f"""
        --- Listar Administradores ---
        {self.conteudo}
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

    def preparar_dados_recebidos(self, dados: list):
        self.dados: list[Usuario] = dados
        for item in self.dados:
            self.conteudo += f"[{item.id_}] - {item.username} \n"


class TelaListarUsuarios(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}
        self.conteudo: str = ""

    def exibir(self):
        mensagem: str = f"""
        --- Listar Usuários ---
        {self.conteudo}
        1 - Visualizar Usuário
        2 - Voltar
        """
        print(mensagem)
        opcao = input("Opção: ")
        return opcao

    def proxima_tela(self, opcao):

        self.transicoes = {
            "visualizar": None,
            "voltar": TelaListar_Gerente(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        self.dados: list[Usuario] = dados
        for item in self.dados:
            self.conteudo += f"[{item.id_}] - {item.tipo} : {item.username} \n"


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

    def preparar_dados_recebidos(self, dados: list):
        pass


class TelaListarLojas(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}
        self.conteudo = ""

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

    def preparar_dados_recebidos(self, dados: list):
        self.dados: list = dados
        for item in self.dados:
            pass
