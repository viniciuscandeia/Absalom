from .tela_escolha_persistencia import TelaEscolhaPersistencia
from .tela_gerenciar_usuarios import TelaGerenciarUsuarios
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
from .telas_listar_usuarios import (
    TelaFiltrarLoja,
    TelaListar_Administrador,
    TelaListar_Gerente,
    TelaListarAdministradores,
    TelaListarLojas,
    TelaListarUsuarios,
)
from .telas_login import TelaLogin, TelaLoginErro
from .tela_opcao_invalida import TelaOpcaoInvalida

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
