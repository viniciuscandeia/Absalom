from ..entidades.entidades_usuarios import Usuario
from ..fabricas.fabrica_repositorios_usuarios import (
    FabricaGerenciadorRepositorioUsuarios,
)
from ..services.autenticacao_usuario import AutenticacaoUsuario
from ..views.estados.gerenciador_telas import GerenciadorTelas
from ..views.estados.view_login import TelaLogin
import os

class Fachada:
    def __init__(self, tipo: str):
        self.repositorio = FabricaGerenciadorRepositorioUsuarios.criar_gerenciador(
            tipo)
        self.telas = GerenciadorTelas(TelaLogin())
        self.autenticador = AutenticacaoUsuario(self.repositorio)
        self.usuario_autenticado = None

    def login(self):
        while True:
            retorno: dict = self.telas.exibir_tela()

            # Autentica o usuário
            self.autenticador.autenticar(
                retorno.get("username", None), retorno.get("senha", None)
            )
            self.usuario_autenticado = self.autenticador.usuario_autenticado()

            # Usuário autenticado
            if self.usuario_autenticado:
                self.telas.proxima_tela(self.usuario_autenticado.tipo)
                self.tela_inicial()
                break  # Sai do loop quando login for bem-sucedido

            # Erro ao logar: exibe tela de erro e volta para a tela de login
            else:
                self.telas.proxima_tela("erro")
                self.telas.exibir_tela()  # Exibe mensagem de erro e tenta novamente
                self.telas.proxima_tela("login")

    def tela_inicial(self):
        while True:
            retorno: dict = self.telas.exibir_tela()

            if self.usuario_autenticado.tipo == "administrador":
                match retorno:
                    case "1":
                        self.telas.proxima_tela("gerenciar_usuarios")
                        self.gerenciar_usuarios()
                    case "2":
                        self.telas.tela_anterior("logout")
                        self.usuario_autenticado = None
                        return  # Sai do método e volta ao login

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
                        self.telas.tela_anterior("logout")
                        self.usuario_autenticado = None
                        return  # Sai do método e volta ao login

            elif self.usuario_autenticado.tipo == "vendedor":
                match retorno:
                    case "1":
                        self.telas.proxima_tela("realizar_venda")
                    case "2":
                        self.telas.tela_anterior("logout")
                        self.usuario_autenticado = None
                        return  # Sai do método e volta ao login

    def gerenciar_usuarios(self):
        while True:
            retorno: dict = self.telas.exibir_tela()

            if self.usuario_autenticado.tipo == "administrador":
                match retorno:

                    case "1":
                        self.telas.proxima_tela(
                            "adicionar_usuario_tela_administrador")
                        self.adicionar_usuario_tela_administrador()
                    case "2":
                        self.telas.proxima_tela()
                    case "3":
                        self.telas.proxima_tela(
                            "listar_usuarios_tela_administrador")
                        self.listar_usuarios_tela_administrador()
                    case "4":
                        self.telas.tela_anterior("administrador")
                        return

            elif self.usuario_autenticado.tipo == "gerente":
                match retorno:

                    case "1":
                        self.telas.proxima_tela(
                            "adicionar_usuario_tela_gerente")
                        self.adicionar_usuario_tela_gerente()
                    case "2":
                        self.telas.proxima_tela()
                    case "3":
                        self.telas.proxima_tela(
                            "listar_usuarios_tela_gerente")
                        self.listar_usuarios_tela_gerente()
                    case "4":
                        self.telas.tela_anterior("voltar_gerente")
                        return

    def adicionar_usuario_tela_administrador(self):
        while True:
            retorno: dict = self.telas.exibir_tela()
            print('aqui 1')

            tipo: str = ''

            match retorno:
                case "1":
                    tipo = 'administrador'
                case "2":
                    tipo = 'gerente'
                case "3":
                    tipo = 'vendedor'
                case "4":
                    self.telas.tela_anterior("voltar")
                    return

            if retorno in ['1', '2', '3']:
                self.telas.proxima_tela(tipo)
                self.adicionar_usuario(tipo)

    def adicionar_usuario_tela_gerente(self, tipo: str):
        while True:
            retorno: dict = self.telas.exibir_tela()

            if retorno in ["1", "2"]:
                self.telas.proxima_tela(tipo)
                self.adicionar_usuario(tipo)
            elif retorno == "3":
                self.telas.tela_anterior("voltar")
                return

    def adicionar_usuario(self, tipo: str):
        while True:
            retorno: dict = self.telas.exibir_tela()

            # Validar entradas
            if True:  # Simulando que as entradas são válidas
                self.adicionar_usuario_sucesso(tipo)
                return
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

    def adicionar_usuario_sucesso(self, tipo: str):
        self.telas.proxima_tela("sucesso")
        self.telas.exibir_tela()

        self.telas.proxima_tela(tipo)
        return

    def adicionar_usuario_erro(self, tipo: str):
        self.telas.exibir_tela()

        self.telas.proxima_tela(tipo)
        self.adicionar_usuario(tipo)

    def listar_usuarios_tela_administrador(self):
        while True:
            retorno: dict = self.telas.exibir_tela()

            match retorno:
                case "1":
                    self.telas.proxima_tela("listar")
                    dados: list[Usuario] = self.repositorio.listar(
                        tipo="administrador")
                    self.telas.enviar_conteudo(dados)
                    self.listar_administradores()
                case "2":
                    self.telas.proxima_tela("filtrar")
                case "3":
                    self.telas.tela_anterior("voltar")
                    return

    def listar_usuarios_tela_gerente(self):
        while True:
            retorno: dict = self.telas.exibir_tela()

            match retorno:
                case "1":
                    self.telas.proxima_tela("listar")
                    dados: list[Usuario] = self.repositorio.listar(
                        id_loja=self.usuario_autenticado.id_loja)
                    self.telas.enviar_conteudo(dados)
                    self.listar_administradores()
                case "2":
                    self.telas.proxima_tela("filtrar")
                case "3":
                    self.telas.tela_anterior("voltar")
                    return

    def listar_administradores(self):
        while True:
            retorno: dict = self.telas.exibir_tela()

            match retorno:
                case '1':
                    self.telas.proxima_tela('visualizar')
                    # * Levar para o método
                case '2':
                    self.telas.tela_anterior('voltar')
                    return

    def listar_usuarios(self):
        while True:
            retorno: dict = self.telas.exibir_tela()

            match retorno:
                case '1':
                    self.telas.proxima_tela('visualizar')
                    # * Levar para o método
                case '2':
                    self.telas.tela_anterior('voltar')
                    return

    def filtrar_por_loja(self):
        pass

    def listar_lojas(self):
        pass
