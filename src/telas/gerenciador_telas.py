from .tela_escolha_persistencia import TelaEscolhaPersistencia
from .tela_gerenciar_usuarios import TelaGerenciarUsuarios
from .tela_opcao_invalida import TelaOpcaoInvalida
from .telas_adicionar_loja import (
    TelaAdicionarLoja,
    TelaAdicionarLojaErroEndereco,
    TelaAdicionarLojaErroNome,
    TelaAdicionarLojaSucesso,
    TelaAssociarLoja,
    TelaAssociarLojaInicial,
)
from .telas_adicionar_usuario import (
    TelaAdicionarAdministrador,
    TelaAdicionarErroEmail,
    TelaAdicionarErroSenha,
    TelaAdicionarErroUsername,
    TelaAdicionarGerente,
    TelaAdicionarSucesso,
    TelaAdicionarUsuarios_Administrador,
    TelaAdicionarUsuarios_Gerente,
    TelaAdicionarVendedor,
)
from .telas_iniciais import (
    TelaInicialAdministrador,
    TelaInicialGerente,
    TelaInicialVendedor,
)
from .telas_listar_lojas import TelaFiltrarLoja, TelaListarLojas, TelaPesquisarLoja, TelaVisualizarLoja
from .telas_listar_usuarios import (
    TelaListar_Administrador,
    TelaListar_Gerente,
    TelaListarAdministradores,
    TelaListarUsuarios,
    TelaPesquisarUsuario,
    TelaVisualizarUsuario,
)
from .telas_login import TelaLogin, TelaLoginErro


class GerenciadorTelas:

    @classmethod
    def escolher_persistencia(cls) -> dict:
        return TelaEscolhaPersistencia.tela()

    @classmethod
    def tela_login(cls) -> dict:
        return TelaLogin.tela()

    @classmethod
    def tela_login_erro(cls) -> None:
        TelaLoginErro.tela()

    @classmethod
    def tela_opcao_invalida(cls) -> None:
        TelaOpcaoInvalida.tela()

    @classmethod
    def tela_inicial_administrador(cls) -> dict:
        return TelaInicialAdministrador.tela()

    @classmethod
    def tela_inicial_gerente(cls) -> dict:
        return TelaInicialGerente.tela()

    @classmethod
    def tela_inicial_vendedor(cls) -> dict:
        return TelaInicialVendedor.tela()

    @classmethod
    def tela_gerenciar_usuarios(cls) -> dict:
        return TelaGerenciarUsuarios.tela()

    @classmethod
    def tela_adicionar_usuario_tela_administrador(cls) -> dict:
        return TelaAdicionarUsuarios_Administrador.tela()

    @classmethod
    def tela_adicionar_usuario_tela_gerente(cls) -> dict:
        return TelaAdicionarUsuarios_Gerente.tela()

    @classmethod
    def tela_adicionar_administrador(cls) -> dict:
        return TelaAdicionarAdministrador.tela()

    @classmethod
    def tela_adicionar_gerente(cls) -> dict:
        return TelaAdicionarGerente.tela()

    @classmethod
    def tela_adicionar_vendedor(cls) -> dict:
        return TelaAdicionarVendedor.tela()

    @classmethod
    def tela_adicionar_usuario_sucesso(cls) -> None:
        TelaAdicionarSucesso.tela()

    @classmethod
    def tela_adicionar_usuario_erro_username(cls) -> None:
        TelaAdicionarErroUsername.tela()

    @classmethod
    def tela_adicionar_usuario_erro_email(cls) -> None:
        TelaAdicionarErroEmail.tela()

    @classmethod
    def tela_adicionar_usuario_erro_senha(cls) -> None:
        TelaAdicionarErroSenha.tela()

    @classmethod
    def tela_associar_loja_inicial(cls) -> dict:
        return TelaAssociarLojaInicial.tela()

    @classmethod
    def tela_adicionar_loja(cls) -> dict:
        return TelaAdicionarLoja.tela()

    @classmethod
    def tela_associar_loja(cls, informacoes: dict) -> dict:
        return TelaAssociarLoja.tela(informacoes)

    @classmethod
    def tela_adicionar_loja_sucesso(cls) -> None:
        return TelaAdicionarLojaSucesso.tela()

    @classmethod
    def tela_adicionar_loja_erro_nome(cls) -> None:
        return TelaAdicionarLojaErroNome.tela()

    @classmethod
    def tela_adicionar_loja_erro_endereco(cls) -> None:
        return TelaAdicionarLojaErroEndereco.tela()

    @classmethod
    def tela_listar_tela_administrador(cls) -> dict:
        return TelaListar_Administrador.tela()

    @classmethod
    def tela_listar_tela_gerente(cls) -> dict:
        return TelaListar_Gerente.tela()

    @classmethod
    def tela_listar_administradores(cls, informacoes: dict) -> dict:
        return TelaListarAdministradores.tela(informacoes)

    @classmethod
    def tela_listar_usuarios(cls, informacoes: dict) -> dict:
        return TelaListarUsuarios.tela(informacoes)

    @classmethod
    def tela_filtrar_por_loja(cls) -> dict:
        return TelaFiltrarLoja.tela()

    @classmethod
    def tela_listar_lojas(cls, informacoes: dict) -> dict:
        return TelaListarLojas.tela(informacoes)

    @classmethod
    def tela_pesquisar_usuario(cls) -> dict:
        return TelaPesquisarUsuario.tela()

    @classmethod
    def tela_visualizar_usuario(cls, usuario) -> dict:
        return TelaVisualizarUsuario.tela(usuario)

    @classmethod
    def tela_pesquisar_tela(cls) -> dict:
        return TelaPesquisarLoja.tela()

    @classmethod
    def tela_visualizar_loja(cls, loja) -> dict:
        return TelaVisualizarLoja.tela(loja)
