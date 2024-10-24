from ..fabricas.fabrica_entidades import FabricaEntidades
from ..fabricas.fabrica_gerenciadores_usuarios import FabricaGerenciadorUsuarios
from ..fabricas.fabrica_repositorio_loja import FabricaGerenciadorLojas
from ..services.autenticacao_usuario import AutenticacaoUsuario
from ..services.validador_informacoes import ValidadorInformacoes
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
        self.gerenciador_lojas = FabricaGerenciadorLojas.criar_gerenciador(
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
            usuario = FabricaEntidades.criar_entidade("administrador", dados)
            self.gerenciador_usuarios.adicionar(usuario)

            dados: dict = {
                "id": self.gerenciador_usuarios.gerar_novo_id(),
                "nome": "gerente",
                "username": "gerente",
                "email": "gerente",
                "senha": "gerente",
                "id_loja": 1,
            }
            usuario = FabricaEntidades.criar_entidade("gerente", dados)
            self.gerenciador_usuarios.adicionar(usuario)

            dados: dict = {
                "id": self.gerenciador_usuarios.gerar_novo_id(),
                "nome": "vendedor",
                "username": "vendedor",
                "email": "vendedor",
                "senha": "vendedor",
                "id_loja": 1,
            }
            usuario = FabricaEntidades.criar_entidade("vendedor", dados)
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
                    if self.usuario_autenticado.tipo == "administrador":
                        self.adicionar_usuario_tela_administrador()
                    else:
                        self.adicionar_usuario_tela_gerente()
                case "2":  # Administrar Usuário
                    pass
                case "3":  # Listar Usuários
                    if self.usuario_autenticado.tipo == "administrador":
                        self.listar_tela_administrador()
                    else:
                        self.listar_tela_gerente()
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
                    self.adicionar_usuario_como_administrador("gerente")
                case "3":  # Adicionar Vendedor
                    self.adicionar_usuario_como_administrador("vendedor")
                case "4":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def adicionar_usuario_tela_gerente(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_usuario_tela_gerente()

            match retorno["opcao"]:
                case "1":  # Adicionar Gerente
                    self.adicionar_usuario_como_gerente("gerente")
                case "2":  # Adicionar Vendedor
                    self.adicionar_usuario_como_gerente("vendedor")
                case "3":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def adicionar_administrador(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_administrador()

            repositorio: dict = self.gerenciador_usuarios.listar()

            # Realizar validação dos dados
            if not ValidadorInformacoes.validacao_username(
                repositorio, retorno["username"]
            ):
                # Erro por causa do username
                GerenciadorTelas.tela_adicionar_usuario_erro_username()
            elif not ValidadorInformacoes.validacao_email(
                repositorio, retorno["email"]
            ):
                # Erro por causa do email
                GerenciadorTelas.tela_adicionar_usuario_erro_email()
            elif not ValidadorInformacoes.validacao_senha(retorno["senha"]):
                # Erro por causa da senha
                GerenciadorTelas.tela_adicionar_usuario_erro_senha()
            else:
                id_novo_usuario: int = self.gerenciador_usuarios.gerar_novo_id()
                retorno["id"] = id_novo_usuario
                usuario = FabricaEntidades.criar_entidade("administrador", retorno)
                self.gerenciador_usuarios.adicionar(usuario)
                GerenciadorTelas.tela_adicionar_usuario_sucesso()
                return

    def adicionar_usuario_como_administrador(self, tipo_usuario: str):
        while True:
            retorno: dict = {}
            if tipo_usuario == "gerente":
                retorno: dict = GerenciadorTelas.tela_adicionar_gerente()
            elif tipo_usuario == "vendedor":
                retorno: dict = GerenciadorTelas.tela_adicionar_vendedor()

            repositorio: dict = self.gerenciador_usuarios.listar()

            # Realizar validação dos dados
            if not ValidadorInformacoes.validacao_username(
                repositorio, retorno["username"]
            ):
                # Erro por causa do username
                GerenciadorTelas.tela_adicionar_usuario_erro_username()
            elif not ValidadorInformacoes.validacao_email(
                repositorio, retorno["email"]
            ):
                # Erro por causa do email
                GerenciadorTelas.tela_adicionar_usuario_erro_email()
            elif not ValidadorInformacoes.validacao_senha(retorno["senha"]):
                # Erro por causa da senha
                GerenciadorTelas.tela_adicionar_usuario_erro_senha()
            else:  # Dados válidos
                id_loja: int = self.associar_loja_tela_inicial()
                id_novo_usuario: int = self.gerenciador_usuarios.gerar_novo_id()
                retorno["id"] = id_novo_usuario
                retorno["id_loja"] = id_loja
                usuario = FabricaEntidades.criar_entidade(tipo_usuario, retorno)
                self.gerenciador_usuarios.adicionar(usuario)
                GerenciadorTelas.tela_adicionar_usuario_sucesso()
                return

    def adicionar_usuario_como_gerente(self, tipo_usuario: str):
        while True:
            retorno: dict = {}
            if tipo_usuario == "gerente":
                retorno: dict = GerenciadorTelas.tela_adicionar_gerente()
            elif tipo_usuario == "vendedor":
                retorno: dict = GerenciadorTelas.tela_adicionar_vendedor()

            repositorio: dict = self.gerenciador_usuarios.listar()

            # Realizar validação dos dados
            if not ValidadorInformacoes.validacao_username(
                repositorio, retorno["username"]
            ):
                # Erro por causa do username
                GerenciadorTelas.tela_adicionar_usuario_erro_username()
            elif not ValidadorInformacoes.validacao_email(
                repositorio, retorno["email"]
            ):
                # Erro por causa do email
                GerenciadorTelas.tela_adicionar_usuario_erro_email()
            elif not ValidadorInformacoes.validacao_senha(retorno["senha"]):
                # Erro por causa da senha
                GerenciadorTelas.tela_adicionar_usuario_erro_senha()
            else:  # Dados válidos
                id_novo_usuario: int = self.gerenciador_usuarios.gerar_novo_id()
                retorno["id"] = id_novo_usuario
                retorno["id_loja"] = self.usuario_autenticado.id_loja
                usuario = FabricaEntidades.criar_entidade(tipo_usuario, retorno)
                self.gerenciador_usuarios.adicionar(usuario)
                GerenciadorTelas.tela_adicionar_usuario_sucesso()
                return

    def associar_loja_tela_inicial(self) -> int:
        while True:
            retorno: dict = GerenciadorTelas.tela_associar_loja_inicial()

            match retorno["opcao"]:
                case "1":  # Adicionar nova loja
                    return self.adicionar_loja()
                case "2":  # Associar com loja existente
                    return self.associar_loja()
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def associar_loja(self) -> int:
        repositorio: dict = self.gerenciador_lojas.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_associar_loja(repositorio)
            if int(retorno["opcao"]) in repositorio.keys():
                return retorno["opcao"]
            else:
                GerenciadorTelas.tela_opcao_invalida()

    def adicionar_loja(self) -> int:
        repositorio: dict = self.gerenciador_lojas.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_loja()

            if not ValidadorInformacoes.validacao_nome_loja(
                repositorio, retorno["nome"]
            ):
                GerenciadorTelas.tela_adicionar_loja_erro_nome()
            elif not ValidadorInformacoes.validacao_endereco(
                repositorio, retorno["endereco"]
            ):
                GerenciadorTelas.tela_adicionar_loja_erro_endereco()
            else:
                id_nova_loja: int = self.gerenciador_lojas.gerar_novo_id()
                retorno["id"] = id_nova_loja
                loja = FabricaEntidades.criar_entidade("loja", retorno)
                self.gerenciador_lojas.adicionar(loja)
                GerenciadorTelas.tela_adicionar_loja_sucesso()
                return id_nova_loja

    def listar_tela_administrador(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_listar_tela_administrador()

            match retorno["opcao"]:
                case "1":  # Listar Administradores
                    self.listar_administradores()
                case "2":  # Filtrar por Loja
                    self.filtrar_loja()
                case "3":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def listar_tela_gerente(self):
        id_loja: int = self.usuario_autenticado.id_loja
        while True:
            retorno: dict = GerenciadorTelas.tela_listar_tela_gerente()

            match retorno["opcao"]:
                case "1":  # Listar usuários
                    self.listar_usuarios(id_loja)
                case "2":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def listar_administradores(self):
        repositorio: dict = self.gerenciador_usuarios.listar(tipo="administrador")

        while True:
            retorno: dict = GerenciadorTelas.tela_listar_administradores(repositorio)

            match retorno["opcao"]:
                case "1":  # Visualizar Administrador
                    self.pesquisar_entidade(repositorio, "usuario")
                case "2":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def listar_usuarios(self, id_loja: int):
        repositorio: dict = self.gerenciador_usuarios.listar(id_loja=id_loja)
        while True:
            retorno: dict = GerenciadorTelas.tela_listar_usuarios(repositorio)

            match retorno["opcao"]:
                case "1":  # Visualizar Usuário
                    self.pesquisar_entidade(repositorio, "usuario")
                case "2":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def filtrar_loja(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_filtrar_por_loja()

            match retorno["opcao"]:
                case "1":  # Listar Lojas
                    self.listar_lojas()
                case "2":  # Pesquisar Loja
                    repositorio: dict = self.gerenciador_lojas.listar()
                    self.pesquisar_entidade(repositorio, "loja")
                case "3":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def listar_lojas(self):
        repositorio: dict = self.gerenciador_lojas.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_listar_lojas(repositorio)

            match retorno["opcao"]:
                case "1":  # Visualizar Loja
                    self.pesquisar_entidade(repositorio, "loja")
                case "2":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def pesquisar_entidade(self, dados: dict, tipo_entidade: str):
        retorno: dict = {}
        while True:
            if tipo_entidade == "usuario":
                retorno: dict = GerenciadorTelas.tela_pesquisar_usuario()
            elif tipo_entidade == "loja":
                retorno: dict = GerenciadorTelas.tela_pesquisar_tela()

            if int(retorno["id"]) in dados.keys():
                self.visualizar_entidade(tipo_entidade, int(retorno["id"]))
                return
            else:  # Opção inválida
                GerenciadorTelas.tela_opcao_invalida()

    def visualizar_entidade(self, tipo_entidade: str, id_: int):

        entidade = None
        if tipo_entidade == "usuario":
            entidade = self.gerenciador_usuarios.buscar(id_)
        elif tipo_entidade == "loja":
            entidade = self.gerenciador_lojas.buscar(id_)

        while True:
            if tipo_entidade == "usuario":
                retorno: dict = GerenciadorTelas.tela_visualizar_usuario(entidade)
            elif tipo_entidade == "loja":
                retorno: dict = GerenciadorTelas.tela_visualizar_loja(entidade)

            match retorno["opcao"]:
                case "1":  # Editar Usuário / Loja
                    pass
                case "2":  # Excluir Usuário / Loja
                    pass
                case "3":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()
