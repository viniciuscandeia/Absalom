from ..fabricas.fabrica_repositorios_usuarios import (
    FabricaGerenciadorRepositorioUsuarios,
)
from ..services.autenticacao_usuario import AutenticacaoUsuario
from ..views.estados.gerenciador_telas import GerenciadorTelas
from ..views.estados.view_login import TelaLogin


class Fachada:
    def __init__(self, tipo: str):
        self.repositorio = FabricaGerenciadorRepositorioUsuarios.criar_gerenciador(tipo)
        self.telas = GerenciadorTelas(TelaLogin())
        self.autenticador = AutenticacaoUsuario(self.repositorio)
        self.usuario_autenticado = None

    def login(self):
        retorno: dict = self.telas.exibir_tela()

        print(retorno)

        self.autenticador.autenticar(
            retorno.get("username", None), retorno.get("senha", None)
        )
        self.usuario_autenticado = self.autenticador.usuario_autenticado()

        print(self.usuario_autenticado)

        # Usuário logado
        if self.usuario_autenticado:
            self.telas.proxima_tela(self.usuario_autenticado.tipo)
            self.tela_inicial()

        # Erro ao logar
        else:
            self.telas.proxima_tela("erro")
            self.telas.exibir_tela()
            self.telas.proxima_tela("login")
            self.login()

    def tela_inicial(self):
        retorno: dict = self.telas.exibir_tela()

        if self.usuario_autenticado.tipo == "administrador":
            match retorno:
                case "1":
                    self.telas.proxima_tela("gerenciar_usuarios")
                    self.gerenciar_usuarios()
                case "2":
                    self.telas.proxima_tela("logout")
                    self.usuario_autenticado = None
                    self.login()

        elif self.usuario_autenticado.tipo == "gerente":
            match retorno:
                case "1":
                    self.telas.proxima_tela("gerenciar_usuarios")
                    self.gerenciar_usuarios()
                case "2":
                    self.telas.proxima_tela("gerenciar_produtos")
                case "3":
                    self.telas.proxima_tela("realizar_venda")
                case "4":
                    self.telas.proxima_tela("logout")
                    self.usuario_autenticado = None
                    self.login()

        elif self.usuario_autenticado.tipo == "vendedor":
            match retorno:
                case "1":
                    self.telas.proxima_tela("realizar_venda")
                case "2":
                    self.telas.proxima_tela("logout")
                    self.usuario_autenticado = None
                    self.login()

    def gerenciar_usuarios(self):
        retorno: dict = self.telas.exibir_tela()

        if self.usuario_autenticado.tipo == "administrador":
            match retorno:

                case "1":
                    self.telas.proxima_tela("adicionar_usuario_tela_administrador")
                    self.adicionar_usuario_tela_administrador()
                case "2":
                    self.telas.proxima_tela()
                case "3":
                    self.telas.proxima_tela()
                case "4":
                    self.telas.proxima_tela("voltar_administrador")
                    self.tela_inicial()

        elif self.usuario_autenticado.tipo == "gerente":
            match retorno:

                case "1":
                    self.telas.proxima_tela("adicionar_usuario_tela_gerente")
                    self.adicionar_usuario_tela_gerente()
                case "2":
                    self.telas.proxima_tela()
                case "3":
                    self.telas.proxima_tela()
                case "4":
                    self.telas.proxima_tela("voltar_gerente")
                    self.tela_inicial()

    def adicionar_usuario_tela_administrador(self):
        retorno: dict = self.telas.exibir_tela()

        match retorno:
            case "1":
                self.telas.proxima_tela("adicionar_administrador")
                self.adicionar_usuario("administrador")
            case "2":
                self.telas.proxima_tela("adicionar_gerente")
                self.adicionar_usuario("gerente")
            case "3":
                self.telas.proxima_tela("adicionar_vendedor")
                self.adicionar_usuario("vendedor")
            case "4":
                self.telas.proxima_tela("voltar")
                self.gerenciar_usuarios()

    def adicionar_usuario_tela_gerente(self):
        retorno: dict = self.telas.exibir_tela()

        match retorno:
            case "1":
                self.telas.proxima_tela("adicionar_gerente")
                self.adicionar_usuario("gerente")
            case "2":
                self.telas.proxima_tela("adicionar_vendedor")
                self.adicionar_usuario("vendedor")
            case "3":
                self.telas.proxima_tela("voltar")
                self.gerenciar_usuarios()

    def adicionar_usuario(self, tipo: str):
        retorno: dict = self.telas.exibir_tela()

        # Validar entradas
        if False:  # Simulando que as entradas são válidas
            self.adicionar_usuario_sucesso()
        else:
            if False:  # Erro username
                self.telas.proxima_tela("erro_username")
                self.adicionar_usuario_erro(tipo)
            if False:
                self.telas.proxima_tela("erro_email")
                self.adicionar_usuario_erro(tipo)
            if True:  # Erro senha
                self.telas.proxima_tela("erro_senha")
                self.adicionar_usuario_erro(tipo)

    def adicionar_usuario_sucesso(self):
        self.telas.proxima_tela("sucesso")
        self.telas.exibir_tela()

        if self.usuario_autenticado.tipo == "administrador":
            self.telas.proxima_tela("voltar_administrador")
            self.adicionar_usuario_tela_administrador()
        elif self.usuario_autenticado.tipo == "gerente":
            self.telas.proxima_tela("voltar_gerente")
            self.adicionar_usuario_tela_administrador()

    def adicionar_usuario_erro(self, tipo: str):
        self.telas.exibir_tela()

        if tipo == "administrador":
            self.telas.proxima_tela("voltar_administrador")
            self.adicionar_usuario(tipo)
        elif tipo == "gerente":
            self.telas.proxima_tela("voltar_gerente")
            self.adicionar_usuario(tipo)
        elif tipo == "vendedor":
            self.telas.proxima_tela("voltar_vendedor")
            self.adicionar_usuario(tipo)
