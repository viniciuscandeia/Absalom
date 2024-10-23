from ..fabricas.fabrica_entidades_usuarios import FabricaEntidadesUsuarios
from ..fabricas.fabrica_gerenciadores_usuarios import FabricaGerenciadorUsuarios
from ..services.autenticacao_usuario import AutenticacaoUsuario
from ..telas.gerenciador_telas import GerenciadorTelas

# * Próximos passos:
#   1 - Realizar validação das entradas (username, email, senha)
#   2 - Considerar se quem está adicionando é um administrador ou um gerente
#       (lógicas diferentes)
#       Adicionando como administrador:
#           Necessário usar uma tela para perguntar se vai querer associar o novo
#           usuário a alguma loja (gerente, vendedor) ou se vai desejar criar uma nova
#           (gerente)
#       Adicionando como gerente:
#       O novo usuário terá o id_loja como o do gerente que está adicionando

class Fachada:

    def __init__(self, tipo_persistencia: str):
        self.gerenciador_usuarios = FabricaGerenciadorUsuarios.criar_gerenciador(
            tipo_persistencia
        )
        self.autenticador = AutenticacaoUsuario(self.gerenciador_usuarios)
        self.usuario_autenticado = None

        # Ao usar a RAM, não terá nenhum usuário cadastrado.
        # Dessa forma, é necessário adicionar, ao menos, um administrador manualmente,
        # para que seja possível utilizar o sistema.

        if tipo_persistencia == "ram":
            dados: dict = {
                "id": self.gerenciador_usuarios.gerar_novo_id(),
                "nome": "admin",
                "username": "admin",
                "email": "admin",
                "senha": "admin",
            }
            usuario = FabricaEntidadesUsuarios.criar_entidade("administrador", dados)
            self.gerenciador_usuarios.adicionar(usuario)

            dados: dict = {
                "id": self.gerenciador_usuarios.gerar_novo_id(),
                "nome": "gerente",
                "username": "gerente",
                "email": "gerente",
                "senha": "gerente",
                "id_loja": 1,
            }
            usuario = FabricaEntidadesUsuarios.criar_entidade("gerente", dados)
            self.gerenciador_usuarios.adicionar(usuario)

            dados: dict = {
                "id": self.gerenciador_usuarios.gerar_novo_id(),
                "nome": "vendedor",
                "username": "vendedor",
                "email": "vendedor",
                "senha": "vendedor",
                "id_loja": 1,
            }
            usuario = FabricaEntidadesUsuarios.criar_entidade("vendedor", dados)
            self.gerenciador_usuarios.adicionar(usuario)

    def login(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_login()

            # Autentica o usuário
            self.autenticador.autenticar(
                retorno.get("username", None), retorno.get("senha", None)
            )
            self.usuario_autenticado = self.autenticador.usuario_autenticado()

            # Usuário autenticado
            if self.usuario_autenticado:
                # Direcionar para a tela certa
                match self.usuario_autenticado.tipo:
                    case "administrador":
                        self.inicial_administrador()
                    case "gerente":
                        self.inicial_gerente()
                    case "vendedor":
                        self.inicial_vendedor()

            # Erro ao logar: exibe tela de erro e volta para a tela de login
            else:
                GerenciadorTelas.tela_login_erro()

    def inicial_administrador(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_inicial_administrador()

            match retorno["opcao"]:
                case "1":  # Gerenciar Usuários
                    self.gerenciar_usuarios()
                case "2":  # Logout
                    self.usuario_autenticado = None
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def inicial_gerente(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_inicial_gerente()

            match retorno["opcao"]:
                case "1":  # Gerenciar Usuários
                    self.gerenciar_usuarios()
                case "2":  # Gerenciar Produtos
                    pass
                case "3":  # Realizar Venda
                    pass
                case "4":  # Logout
                    self.usuario_autenticado = None
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def inicial_vendedor(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_inicial_vendedor()

            match retorno["opcao"]:
                case "1":  # Realizar Venda
                    pass
                case "2":  # Logout
                    self.usuario_autenticado = None
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def gerenciar_usuarios(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_gerenciar_usuarios()

            match retorno["opcao"]:
                case "1":  # Adicionar Usuário
                    pass
                case "2":  # Administrar Usuário
                    pass
                case "3":  # Listar Usuários
                    pass
                case "4":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def adicionar_usuario_tela_administrador(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_usuario_tela_administrador()

            match retorno["opcao"]:
                case "1":  # Adicionar Administrador
                    self.adicionar_administrador()
                case "2":  # Adicionar Gerente
                    self.adicionar_gerente()
                case "3":  # Adicionar Vendedor
                    self.adicionar_vendedor()
                case "4":  # Voltar
                    pass
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def adicionar_usuario_tela_gerente(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_usuario_tela_gerente()

            match retorno["opcao"]:
                case "1":  # Adicionar Gerente
                    self.adicionar_gerente()
                case "2":  # Adicionar Vendedor
                    self.adicionar_vendedor()
                case "3":  # Voltar
                    pass
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def adicionar_administrador(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_administrador()

            # Realizar validação dos dados
            if True:  # Erro por causa do username
                GerenciadorTelas.tela_adicionar_usuario_erro_username()
            elif True:  # Erro por causa do email
                GerenciadorTelas.tela_adicionar_usuario_erro_email()
            elif True:  # Erro por causa da senha
                GerenciadorTelas.tela_adicionar_usuario_erro_senha()
            else:  # Dados válidos
                id_novo_usuario: int = self.gerenciador_usuarios.gerar_novo_id()
                retorno["id"] = id_novo_usuario
                usuario = FabricaEntidadesUsuarios.criar_entidade(
                    "administrador", retorno
                )
                self.gerenciador_usuarios.adicionar(usuario)
                GerenciadorTelas.tela_adicionar_usuario_sucesso()

    def adicionar_gerente(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_gerente()

            # Duas situações:
            # Se for um gerente adicionando outro gerente
            # Se for um administrador adicionando
            #   Tela perguntando a qual loja ele será associado (ou se vai criar uma)

            # Realizar validação dos dados
            if True:  # Erro por causa do username
                GerenciadorTelas.tela_adicionar_usuario_erro_username()
            elif True:  # Erro por causa do email
                GerenciadorTelas.tela_adicionar_usuario_erro_email()
            elif True:  # Erro por causa da senha
                GerenciadorTelas.tela_adicionar_usuario_erro_senha()
            else:  # Dados válidos
                id_novo_usuario: int = self.gerenciador_usuarios.gerar_novo_id()
                retorno["id"] = id_novo_usuario
                usuario = FabricaEntidadesUsuarios.criar_entidade("gerente", retorno)
                self.gerenciador_usuarios.adicionar(usuario)
                GerenciadorTelas.tela_adicionar_usuario_sucesso()

    def adicionar_vendedor(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_vendedor()

            # Duas situações:
            # Se for um gerente adicionando um vendedor
            # Se for um administrador adicionando
            #   Tela perguntando a qual loja ele será associado

            # Realizar validação dos dados
            if True:  # Erro por causa do username
                GerenciadorTelas.tela_adicionar_usuario_erro_username()
            elif True:  # Erro por causa do email
                GerenciadorTelas.tela_adicionar_usuario_erro_email()
            elif True:  # Erro por causa da senha
                GerenciadorTelas.tela_adicionar_usuario_erro_senha()
            else:  # Dados válidos
                id_novo_usuario: int = self.gerenciador_usuarios.gerar_novo_id()
                retorno["id"] = id_novo_usuario
                usuario = FabricaEntidadesUsuarios.criar_entidade("vendedor", retorno)
                self.gerenciador_usuarios.adicionar(usuario)
                GerenciadorTelas.tela_adicionar_usuario_sucesso()
