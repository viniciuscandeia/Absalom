from ..fabricas.fabrica_entidades import FabricaEntidades
from ..fabricas.fabrica_gerenciadores_usuarios import FabricaGerenciadorUsuarios
from ..fabricas.fabrica_repositorio_loja import FabricaGerenciadorLojas
from ..fabricas.fabrica_repositorio_produto import FabricaGerenciadorProdutos
from ..services.autenticacao_usuario import AutenticacaoUsuario
from ..services.validador_informacoes import ValidadorInformacoes
from ..telas.gerenciador_telas import GerenciadorTelas

# * Possível uso do Observer para ficar analisando alguma mudança no banco de dados
# Garantir que exista sempre ao menos 1 gerente por loja (a restrição não se aplica a vendedor)
# * Trocar nome de fabrica_repositorio_loja para fabrica_gerenciadores_loja (o mesmo para produto)
# As entidades têm alguns métodos similares (confirmação, descartar). Poderiam usar o mesmo método.


class Fachada:

    def __init__(self, tipo_persistencia: str):
        self.gerenciador_usuarios = FabricaGerenciadorUsuarios.criar_gerenciador(
            tipo_persistencia
        )
        self.gerenciador_lojas = FabricaGerenciadorLojas.criar_gerenciador(
            tipo_persistencia
        )
        self.gerenciador_produtos = FabricaGerenciadorProdutos.criar_gerenciador(
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
                    self.gerenciar_usuarios_como_administrador()
                case "2":  # Gerenciar Lojas
                    self.gerenciar_lojas()
                case "3":  # Logout
                    self.usuario_autenticado = None
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def inicial_gerente(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_inicial_gerente()

            match retorno["opcao"]:
                case "1":  # Gerenciar Usuários
                    self.gerenciar_funcionarios()
                case "2":  # Gerenciar Produtos
                    self.gerenciar_produtos(self.usuario_autenticado.id_loja)
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

    def gerenciar_usuarios_como_administrador(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_gerenciar_usuarios()

            match retorno["opcao"]:
                case "1":  # Adicionar Usuário
                    self.adicionar_usuario_tela_administrador()
                case "2":  # Administrar Usuário
                    repositorio: dict = self.gerenciador_usuarios.listar()
                    self.pesquisar_entidade(repositorio, "usuario")
                case "3":  # Listar Usuários
                    self.listar_tela_administrador()
                case "4":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def gerenciar_funcionarios(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_gerenciar_usuarios()

            match retorno["opcao"]:
                case "1":  # Adicionar Usuário
                    self.adicionar_usuario_tela_gerente()
                case "2":  # Administrar Usuário
                    repositorio: dict = self.gerenciador_usuarios.listar(
                        id_loja=self.usuario_autenticado.id_loja
                    )
                    self.pesquisar_entidade(repositorio, "usuario")
                case "3":  # Listar Usuários
                    self.listar_tela_gerente()
                case "4":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def gerenciar_lojas(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_gerenciar_lojas()

            match retorno["opcao"]:
                case "1":  # Administrar Loja
                    repositorio: dict = self.gerenciador_lojas.listar()
                    self.pesquisar_entidade(repositorio, "loja")
                case "2":  # Listar Lojas
                    self.listar_lojas()
                case "3":
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def gerenciar_produtos(self, id_loja: int):
        while True:
            retorno: dict = GerenciadorTelas.tela_gerenciar_produtos()

            match retorno["opcao"]:
                case "1":  # Adicionar Produto
                    self.adicionar_produto(id_loja)
                case "2":  # Administrar Produto
                    repositorio: dict = self.gerenciador_produtos.listar(id_loja)
                    self.pesquisar_entidade(repositorio, "produto")
                case "3":  # Listar Produtos
                    self.listar_produtos(id_loja)
                case "4":
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
                    self.filtrar_usuarios_por_loja()
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
                    repositorio: dict = self.gerenciador_usuarios.listar(
                        tipo="administrador"
                    )
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
                    repositorio: dict = self.gerenciador_usuarios.listar(
                        id_loja=id_loja
                    )
                case "2":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def filtrar_usuarios_por_loja(self):
        while True:
            retorno: dict = GerenciadorTelas.tela_filtrar_por_loja()

            match retorno["opcao"]:
                case "1":  # Listar Lojas
                    self.listar_lojas_fluxo_filtro()
                case "2":  # Pesquisar Loja
                    repositorio: dict = self.gerenciador_lojas.listar()
                    self.pesquisar_loja_fluxo_filtro(repositorio)
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
                    repositorio: dict = self.gerenciador_lojas.listar()
                case "2":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def listar_lojas_fluxo_filtro(self):
        repositorio: dict = self.gerenciador_lojas.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_listar_lojas_fluxo_filtro(repositorio)

            match retorno["opcao"]:
                case "1":  # Visualizar Loja
                    self.pesquisar_loja_fluxo_filtro(repositorio)
                    repositorio: dict = self.gerenciador_lojas.listar()
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
                retorno: dict = GerenciadorTelas.tela_pesquisar_loja()
            elif tipo_entidade == "produto":
                retorno: dict = GerenciadorTelas.tela_pesquisar_produto()

            if str(retorno["id"]).isdigit():
                if int(retorno["id"]) in dados.keys():
                    if tipo_entidade == "usuario":
                        self.visualizar_usuario(int(retorno["id"]))
                    if tipo_entidade == "loja":
                        self.visualizar_loja(int(retorno["id"]))
                    if tipo_entidade == "produto":
                        self.visualizar_produto(int(retorno["id"]))
                    return
            else:  # Opção inválida
                GerenciadorTelas.tela_opcao_invalida()

    def pesquisar_loja_fluxo_filtro(self, dados: dict):
        retorno: dict = {}
        while True:
            retorno: dict = GerenciadorTelas.tela_pesquisar_loja()

            if str(retorno["id"]).isdigit():
                if int(retorno["id"]) in dados.keys():
                    self.listar_usuarios(int(retorno["id"]))
                    return
            else:  # Opção inválida
                GerenciadorTelas.tela_opcao_invalida()

    def visualizar_usuario(self, id_: int):

        entidade = self.gerenciador_usuarios.buscar(id_)

        while True:
            retorno: dict = GerenciadorTelas.tela_visualizar_usuario(entidade)

            match retorno["opcao"]:
                case "1":  # Editar Usuário
                    informacoes: dict = {}
                    informacoes["id"] = entidade.id_
                    informacoes["nome"] = entidade.nome
                    informacoes["username"] = entidade.username
                    informacoes["email"] = entidade.email
                    informacoes["senha"] = entidade.senha
                    informacoes["tipo"] = entidade.tipo
                    informacoes["id_loja"] = entidade.id_loja
                    self.editar_usuario(informacoes)
                    entidade = self.gerenciador_usuarios.buscar(id_)

                case "2":  # Excluir Usuário
                    resultado: bool = self.excluir_usuario()
                    if resultado:
                        self.gerenciador_usuarios.remover(entidade.id_)
                        GerenciadorTelas.tela_excluir_usuario_sucesso()
                        return

                case "3":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def visualizar_loja(self, id_: int):

        entidade = self.gerenciador_lojas.buscar(id_)

        while True:
            retorno: dict = GerenciadorTelas.tela_visualizar_loja(entidade)

            match retorno["opcao"]:
                case "1":  # Gerenciar Funcionários
                    self.gerenciar_funcionarios()
                case "2":  # Gerenciar Produtos
                    self.gerenciar_produtos(id_)
                case "3":  # Editar Loja
                    informacoes: dict = {}
                    informacoes["id"] = entidade.id_
                    informacoes["nome"] = entidade.nome
                    informacoes["endereco"] = entidade.endereco
                    self.editar_loja(informacoes)
                    entidade = self.gerenciador_lojas.buscar(id_)
                case "4":  # Excluir Loja
                    resultado: bool = self.excluir_loja()
                    if resultado:
                        self.gerenciador_lojas.remover(entidade.id_)
                        GerenciadorTelas.tela_excluir_loja_sucesso()
                        return
                case "5":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def visualizar_produto(self, id_: int):

        entidade = self.gerenciador_produtos.buscar(id_)

        while True:
            retorno: dict = GerenciadorTelas.tela_visualizar_produto(entidade)

            match retorno["opcao"]:
                case "1":  # Editar Produto
                    informacoes: dict = {}
                    informacoes["id"] = entidade.id_
                    informacoes["nome"] = entidade.nome
                    informacoes["descricao"] = entidade.descricao
                    informacoes["preco"] = entidade.preco
                    informacoes["quantidade"] = entidade.quantidade
                    informacoes["id_loja"] = entidade.id_loja
                    self.editar_produto(informacoes)
                    entidade = self.gerenciador_produtos.buscar(id_)
                case "2":  # Excluir Produto
                    resultado: bool = self.excluir_produto()
                    if resultado:
                        self.gerenciador_produtos.remover(entidade.id_)
                        GerenciadorTelas.tela_excluir_produto_sucesso()
                        return
                case "3":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_usuario(self, informacoes: dict):

        novas_informacoes: dict = informacoes.copy()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_usuario(novas_informacoes)

            match retorno["opcao"]:
                case "1":  # Editar Nome
                    novo_nome: str = self.editar_usuario_nome(novas_informacoes["nome"])
                    novas_informacoes["nome"] = novo_nome
                case "2":  # Editar Username
                    novo_username: str = self.editar_usuario_username(
                        novas_informacoes["username"]
                    )
                    novas_informacoes["username"] = novo_username
                case "3":  # Editar Email
                    novo_email: str = self.editar_usuario_email(
                        novas_informacoes["email"]
                    )
                    novas_informacoes["email"] = novo_email
                case "4":  # Confirmar edição
                    resultado: bool = self.editar_usuario_confirmacao(novas_informacoes)
                    if resultado:
                        return
                case "5":  # Descartar edição
                    resultado: bool = self.editar_usuario_descartar()
                    if resultado:
                        return
                case "6":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_usuario_nome(self, nome: str) -> str:
        retorno: dict = GerenciadorTelas.tela_editar_usuario_nome(nome)
        if retorno["nome"] != "":
            return retorno["nome"]
        return nome

    def editar_usuario_username(self, username: str) -> str:
        repositorio: dict = self.gerenciador_usuarios.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_usuario_username(username)
            if retorno["username"] != "":
                if not ValidadorInformacoes.validacao_username(
                    repositorio, retorno["username"]
                ):
                    GerenciadorTelas.tela_editar_usuario_erro_username()
                else:
                    return retorno["username"]
            else:
                return username

    def editar_usuario_email(self, email: str) -> str:
        repositorio: dict = self.gerenciador_usuarios.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_usuario_email(email)
            if retorno["email"] != "":
                if not ValidadorInformacoes.validacao_email(
                    repositorio, retorno["email"]
                ):
                    GerenciadorTelas.tela_editar_usuario_erro_email()
                else:
                    return retorno["email"]
            else:
                return email

    def editar_usuario_confirmacao(self, informacoes: dict) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_usuario_confirmacao()

            match retorno["opcao"]:
                case "1":  # Confirmar
                    usuario = FabricaEntidades.criar_entidade(
                        informacoes["tipo"], informacoes
                    )
                    self.gerenciador_usuarios.editar(informacoes["id"], usuario)
                    GerenciadorTelas.tela_editar_usuario_sucesso()
                    return True
                case "2":  # Voltar
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_usuario_descartar(self) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_usuario_descartar()

            match retorno["opcao"]:
                case "1":  # Descartar
                    return True
                case "2":  # Voltar
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def excluir_usuario(self) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_excluir_usuario()

            match retorno["opcao"]:
                case "1":
                    return True
                case "2":
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_loja(self, informacoes: dict):

        novas_informacoes: dict = informacoes.copy()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_loja(novas_informacoes)

            match retorno["opcao"]:
                case "1":  # Editar Nome
                    novo_nome: str = self.editar_loja_nome(novas_informacoes["nome"])
                    novas_informacoes["nome"] = novo_nome
                case "2":  # Editar Endereço
                    novo_endereco: str = self.editar_loja_endereco(
                        novas_informacoes["endereco"]
                    )
                    novas_informacoes["endereco"] = novo_endereco
                case "3":  # Confirmar edição
                    resultado: bool = self.editar_loja_confirmacao(novas_informacoes)
                    if resultado:
                        return
                case "4":  # Descartar edição
                    resultado: bool = self.editar_loja_descartar()
                    if resultado:
                        return
                case "5":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_loja_nome(self, nome: str) -> str:
        repositorio: dict = self.gerenciador_lojas.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_loja_nome(nome)
            if retorno["nome"] != "":
                if not ValidadorInformacoes.validacao_nome_loja(
                    repositorio, retorno["nome"]
                ):
                    GerenciadorTelas.tela_editar_loja_erro_nome()
                else:
                    return retorno["nome"]
            else:
                return nome

    def editar_loja_endereco(self, endereco: str) -> str:
        repositorio: dict = self.gerenciador_lojas.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_loja_endereco(endereco)
            if retorno["endereco"] != "":
                if not ValidadorInformacoes.validacao_endereco(
                    repositorio, retorno["endereco"]
                ):
                    GerenciadorTelas.tela_editar_loja_erro_endereco()
                else:
                    return retorno["endereco"]
            else:
                return endereco

    def editar_loja_confirmacao(self, informacoes: dict) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_loja_confirmacao()

            match retorno["opcao"]:
                case "1":  # Confirmar
                    loja = FabricaEntidades.criar_entidade("loja", informacoes)
                    self.gerenciador_lojas.editar(informacoes["id"], loja)
                    GerenciadorTelas.tela_editar_loja_sucesso()
                    return True
                case "2":  # Voltar
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_loja_descartar(self) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_loja_descartar()

            match retorno["opcao"]:
                case "1":  # Descartar
                    return True
                case "2":  # Voltar
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def excluir_loja(self) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_excluir_loja()

            match retorno["opcao"]:
                case "1":
                    return True
                case "2":
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    # * Adicionar produto

    def adicionar_produto(self, id_loja: int) -> None:
        repositorio: dict = self.gerenciador_produtos.listar(id_loja)
        while True:
            retorno: dict = GerenciadorTelas.tela_adicionar_produto()
            if not ValidadorInformacoes.validacao_produto_nome(
                repositorio, retorno["nome"]
            ):
                # Erro por causa do nome
                GerenciadorTelas.tela_adicionar_produto_erro_nome()

            elif not ValidadorInformacoes.validacao_produto_descricao(
                retorno["descricao"]
            ):
                # Erro por causa da descrição
                GerenciadorTelas.tela_adicionar_produto_erro_descricao()

            elif not ValidadorInformacoes.validacao_produto_preco(retorno["preco"]):
                # Erro por causa do preço
                GerenciadorTelas.tela_adicionar_produto_erro_preco()

            elif not ValidadorInformacoes.validacao_produto_quantidade(
                retorno["quantidade"]
            ):
                # Erro por causa da quantidade
                GerenciadorTelas.tela_adicionar_produto_erro_quantidade()

            else:  # Informações válidas
                id_novo_produto: int = self.gerenciador_produtos.gerar_novo_id()
                retorno["id"] = id_novo_produto
                retorno["id_loja"] = id_loja
                produto = FabricaEntidades.criar_entidade("produto", retorno)
                self.gerenciador_produtos.adicionar(produto)
                GerenciadorTelas.tela_adicionar_produto_sucesso()
                return

    # * Listar produtos

    def editar_produto(self, informacoes: dict) -> None:
        novas_informacoes: dict = informacoes.copy()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_produto(novas_informacoes)

            match retorno["opcao"]:
                case "1":  # Editar Nome
                    novo_nome: str = self.editar_produto_nome(novas_informacoes["nome"])
                    novas_informacoes["nome"] = novo_nome
                case "2":  # Editar Descrição
                    nova_descricao: str = self.editar_produto_descricao(
                        novas_informacoes["descricao"]
                    )
                    novas_informacoes["username"] = nova_descricao
                case "3":  # Editar Preço
                    novo_preco: str = self.editar_produto_preco(
                        novas_informacoes["preco"]
                    )
                    novas_informacoes["preco"] = novo_preco
                case "4":  # Editar Quantidade
                    nova_quantidade: str = self.editar_produto_quantidade(
                        novas_informacoes["quantidade"]
                    )
                    novas_informacoes["quantidade"] = nova_quantidade
                case "5":  # Confirmar edição
                    resultado: bool = self.editar_produto_confirmacao(novas_informacoes)
                    if resultado:
                        return
                case "6":  # Descartar edição
                    resultado: bool = self.editar_produto_descartar()
                    if resultado:
                        return
                case "7":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_produto_nome(self, nome: str) -> str:
        repositorio: dict = self.gerenciador_produtos.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_produto_nome(nome)
            if retorno["nome"] != "":
                if not ValidadorInformacoes.validacao_produto_nome(
                    repositorio, retorno["nome"]
                ):
                    GerenciadorTelas.tela_editar_produto_erro_nome()
                else:
                    return retorno["nome"]
            else:
                return nome

    def editar_produto_descricao(self, descricao: str) -> str:
        retorno: dict = GerenciadorTelas.tela_editar_produto_descricao(descricao)
        if retorno["descricao"] != "":
            return retorno["descricao"]
        return descricao

    def editar_produto_preco(self, preco: str) -> str:
        repositorio: dict = self.gerenciador_produtos.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_produto_preco(preco)
            if retorno["preco"] != "":
                if not ValidadorInformacoes.validacao_produto_preco(
                    repositorio, retorno["preco"]
                ):
                    GerenciadorTelas.tela_editar_produto_erro_preco()
                else:
                    return retorno["preco"]
            else:
                return preco

    def editar_produto_quantidade(self, quantidade: str) -> str:
        repositorio: dict = self.gerenciador_produtos.listar()
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_produto_quantidade(quantidade)
            if retorno["quantidade"] != "":
                if not ValidadorInformacoes.validacao_produto_quantidade(
                    repositorio, retorno["quantidade"]
                ):
                    GerenciadorTelas.tela_editar_produto_erro_quantidade()
                else:
                    return retorno["quantidade"]
            else:
                return quantidade

    def editar_produto_confirmacao(self, informacoes: dict) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_produto_confirmacao()

            match retorno["opcao"]:
                case "1":  # Confirmar
                    produto = FabricaEntidades.criar_entidade("produto", informacoes)
                    self.gerenciador_produtos.editar(informacoes["id"], produto)
                    GerenciadorTelas.tela_editar_produto_sucesso()
                    return True
                case "2":  # Voltar
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    def editar_produto_descartar(self) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_editar_produto_descartar()

            match retorno["opcao"]:
                case "1":  # Descartar
                    return True
                case "2":  # Voltar
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    # * Excluir produto

    def excluir_produto(self) -> bool:
        while True:
            retorno: dict = GerenciadorTelas.tela_excluir_produto()

            match retorno["opcao"]:
                case "1":
                    return True
                case "2":
                    return False
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()

    # * Listar produtos

    def listar_produtos(self, id_loja):
        repositorio: dict = self.gerenciador_produtos.listar(id_loja)
        while True:
            retorno: dict = GerenciadorTelas.tela_listar_produtos(repositorio)

            match retorno["opcao"]:
                case "1":  # Visualizar Produto
                    self.pesquisar_entidade(repositorio, "produto")
                    repositorio: dict = self.gerenciador_produtos.listar(id_loja)
                case "2":  # Voltar
                    return
                case _:  # Opção inválida
                    GerenciadorTelas.tela_opcao_invalida()
