from ..entidades.entidades_usuarios import Usuario
from .comando_adicionar_loja import AdicionarLojaComando
from .comando_adicionar_produto import AdicionarProdutoComando
from .comando_adicionar_usuario import AdicionarUsuarioComando
from .comando_editar_loja import EditarLojaComando
from .comando_editar_produto import EditarProdutoComando
from .comando_editar_usuario import EditarUsuarioComando
from .comando_enviar_notificacao import EnviarNotificacaoComando
from .comando_excluir_loja import ExcluirLojaComando
from .comando_excluir_produto import ExcluirProdutoComando
from .comando_excluir_usuario import ExcluirUsuarioComando
from .comando_login import ComandoLogin
from .comando_ver_notificacoes import VerNotificacoesComando
from .invocador import Invocador


class GerenciadorComandos:

    @classmethod
    def comando_autenticar_usuario(
        cls, autenticador, username: str, senha: str
    ) -> Usuario:
        comando = ComandoLogin(autenticador, username, senha)
        return Invocador.executar_comando(comando)

    @classmethod
    def comando_adicionar_usuario(cls, gerenciador_usuarios, usuario):
        comando = AdicionarUsuarioComando(gerenciador_usuarios, usuario)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_adicionar_loja(cls, gerenciador_lojas, loja):
        comando = AdicionarLojaComando(gerenciador_lojas, loja)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_adicionar_produto(cls, gerenciador_produtos, produto):
        comando = AdicionarProdutoComando(gerenciador_produtos, produto)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_editar_usuario(cls, gerenciador_usuarios, id_usuario: int, usuario):
        comando = EditarUsuarioComando(gerenciador_usuarios, id_usuario, usuario)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_editar_loja(
        cls, gerenciador_lojas, id_loja: int, loja, id_usuario: int
    ):
        comando = EditarLojaComando(gerenciador_lojas, id_loja, loja, id_usuario)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_editar_produto(cls, gerenciador_produtos, id_produto: int, produto):
        comando = EditarProdutoComando(gerenciador_produtos, id_produto, produto)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_excluir_usuario(cls, gerenciador_usuarios, id_usuario: int):
        comando = ExcluirUsuarioComando(gerenciador_usuarios, id_usuario)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_excluir_loja(cls, gerenciador_lojas, id_loja: int):
        comando = ExcluirLojaComando(gerenciador_lojas, id_loja)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_excluir_produto(cls, gerenciador_produtos, id_produto: int):
        comando = ExcluirProdutoComando(gerenciador_produtos, id_produto)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_enviar_notificacao(cls, loja, id_usuario: int):
        comando = EnviarNotificacaoComando(loja=loja, id_usuario=id_usuario)
        Invocador.executar_comando(comando)

    @classmethod
    def comando_listar_notificacoes(cls, loja, id_loja):
        comando = VerNotificacoesComando(id_loja=id_loja)
        return Invocador.executar_comando(comando)
