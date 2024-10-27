from .tela_escolha_persistencia import TelaEscolhaPersistencia
from .tela_gerenciar_lojas import TelaGerenciarLojas
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
from .telas_adicionar_produto import (
    TelaAdicionarProduto,
    TelaAdicionarProdutoErroDescricao,
    TelaAdicionarProdutoErroNome,
    TelaAdicionarProdutoErroPreco,
    TelaAdicionarProdutoErroQuantidade,
    TelaAdicionarProdutoSucesso,
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
from .telas_editar_loja import (
    TelaEditarLoja,
    TelaEditarLojaConfirmacao,
    TelaEditarLojaDescartar,
    TelaEditarLojaEndereco,
    TelaEditarLojaErroEndereco,
    TelaEditarLojaErroNome,
    TelaEditarLojaNome,
    TelaEditarLojaSucesso,
)
from .telas_editar_produto import (
    TelaEditarProduto,
    TelaEditarProdutoConfirmacao,
    TelaEditarProdutoDescartar,
    TelaEditarProdutoDescricao,
    TelaEditarProdutoErroNome,
    TelaEditarProdutoErroPreco,
    TelaEditarProdutoErroQuantidade,
    TelaEditarProdutoNome,
    TelaEditarProdutoPreco,
    TelaEditarProdutoQuantidade,
    TelaEditarProdutoSucesso,
)
from .telas_editar_usuarios import (
    TelaEditarUsuario,
    TelaEditarUsuarioConfirmacao,
    TelaEditarUsuarioDescartar,
    TelaEditarUsuarioEmail,
    TelaEditarUsuarioErroEmail,
    TelaEditarUsuarioErroUsername,
    TelaEditarUsuarioNome,
    TelaEditarUsuarioSucesso,
    TelaEditarUsuarioUsername,
)
from .telas_excluir_loja import TelaExcluirLoja, TelaExcluirLojaSucesso
from .telas_excluir_produto import TelaExcluirProduto, TelaExcluirProdutoSucesso
from .telas_excluir_usuario import TelaExcluirUsuario, TelaExcluirUsuarioSucesso
from .telas_iniciais import (
    TelaInicialAdministrador,
    TelaInicialGerente,
    TelaInicialVendedor,
)
from .telas_listar_lojas import (
    TelaFiltrarLoja,
    TelaListarLojas,
    TelaListarLojasFluxoFiltro,
    TelaPesquisarLoja,
    TelaVisualizarLoja,
)
from .telas_listar_usuarios import (
    TelaListar_Administrador,
    TelaListar_Gerente,
    TelaListarAdministradores,
    TelaListarUsuarios,
    TelaPesquisarUsuario,
    TelaVisualizarUsuario,
)
from .telas_listas_produtos import (
    TelaListarProdutos,
    TelaPesquisarProduto,
    TelaVisualizarProduto,
)
from .telas_login import TelaLogin, TelaLoginErro
from .tela_gerenciar_produtos import TelaGerenciarProdutos

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
    def tela_listar_lojas_fluxo_filtro(cls, informacoes: dict) -> dict:
        return TelaListarLojasFluxoFiltro.tela(informacoes)

    @classmethod
    def tela_pesquisar_usuario(cls) -> dict:
        return TelaPesquisarUsuario.tela()

    @classmethod
    def tela_visualizar_usuario(cls, usuario) -> dict:
        return TelaVisualizarUsuario.tela(usuario)

    @classmethod
    def tela_pesquisar_loja(cls) -> dict:
        return TelaPesquisarLoja.tela()

    @classmethod
    def tela_visualizar_loja(cls, loja) -> dict:
        return TelaVisualizarLoja.tela(loja)

    @classmethod
    def tela_editar_usuario(cls, informacoes: dict) -> dict:
        return TelaEditarUsuario.tela(informacoes)

    @classmethod
    def tela_editar_usuario_nome(cls, nome: str) -> dict:
        return TelaEditarUsuarioNome.tela(nome)

    @classmethod
    def tela_editar_usuario_username(cls, username: str) -> dict:
        return TelaEditarUsuarioUsername.tela(username)

    @classmethod
    def tela_editar_usuario_email(cls, email: str) -> dict:
        return TelaEditarUsuarioEmail.tela(email)

    @classmethod
    def tela_editar_usuario_confirmacao(cls) -> dict:
        return TelaEditarUsuarioConfirmacao.tela()

    @classmethod
    def tela_editar_usuario_descartar(cls) -> dict:
        return TelaEditarUsuarioDescartar.tela()

    @classmethod
    def tela_editar_usuario_erro_username(cls) -> None:
        TelaEditarUsuarioErroUsername.tela()

    @classmethod
    def tela_editar_usuario_erro_email(cls) -> None:
        TelaEditarUsuarioErroEmail.tela()

    @classmethod
    def tela_editar_usuario_sucesso(cls) -> None:
        TelaEditarUsuarioSucesso.tela()

    @classmethod
    def tela_excluir_usuario(cls) -> dict:
        return TelaExcluirUsuario.tela()

    @classmethod
    def tela_excluir_usuario_sucesso(cls) -> None:
        TelaExcluirUsuarioSucesso.tela()

    @classmethod
    def tela_editar_loja(cls, informacoes: dict) -> dict:
        return TelaEditarLoja.tela(informacoes)

    @classmethod
    def tela_editar_loja_nome(cls, nome: str) -> dict:
        return TelaEditarLojaNome.tela(nome)

    @classmethod
    def tela_editar_loja_endereco(cls, endereco: str) -> dict:
        return TelaEditarLojaEndereco.tela(endereco)

    @classmethod
    def tela_editar_loja_confirmacao(cls) -> dict:
        return TelaEditarLojaConfirmacao.tela()

    @classmethod
    def tela_editar_loja_descartar(cls) -> dict:
        return TelaEditarLojaDescartar.tela()

    @classmethod
    def tela_editar_loja_erro_nome(cls) -> None:
        TelaEditarLojaErroNome.tela()

    @classmethod
    def tela_editar_loja_erro_endereco(cls) -> None:
        TelaEditarLojaErroEndereco.tela()

    @classmethod
    def tela_editar_loja_sucesso(cls) -> None:
        TelaEditarLojaSucesso.tela()

    @classmethod
    def tela_excluir_loja(cls) -> dict:
        return TelaExcluirLoja.tela()

    @classmethod
    def tela_excluir_loja_sucesso(cls) -> None:
        TelaExcluirLojaSucesso.tela()

    # * Gerenciar Lojas

    @classmethod
    def tela_gerenciar_lojas(cls) -> dict:
        return TelaGerenciarLojas.tela()

    # * Gerenciar Produtos

    @classmethod
    def tela_gerenciar_produtos(cls) -> dict:
        return TelaGerenciarProdutos.tela()

    # * Adicionar produto

    @classmethod
    def tela_adicionar_produto(cls) -> dict:
        return TelaAdicionarProduto.tela()

    @classmethod
    def tela_adicionar_produto_sucesso(cls) -> None:
        TelaAdicionarProdutoSucesso.tela()

    @classmethod
    def tela_adicionar_produto_erro_nome(cls) -> None:
        TelaAdicionarProdutoErroNome.tela()

    @classmethod
    def tela_adicionar_produto_erro_descricao(cls) -> None:
        TelaAdicionarProdutoErroDescricao.tela()

    @classmethod
    def tela_adicionar_produto_erro_preco(cls) -> None:
        TelaAdicionarProdutoErroPreco.tela()

    @classmethod
    def tela_adicionar_produto_erro_quantidade(cls) -> None:
        TelaAdicionarProdutoErroQuantidade.tela()

    # * Editar produto

    @classmethod
    def tela_editar_produto(cls, informacoes: dict) -> dict:
        return TelaEditarProduto.tela(informacoes)

    @classmethod
    def tela_editar_produto_nome(cls, nome: str) -> dict:
        return TelaEditarProdutoNome.tela(nome)

    @classmethod
    def tela_editar_produto_descricao(cls, descricao: str) -> dict:
        return TelaEditarProdutoDescricao.tela(descricao)

    @classmethod
    def tela_editar_produto_preco(cls, preco: str) -> dict:
        return TelaEditarProdutoPreco.tela(preco)

    @classmethod
    def tela_editar_produto_quantidade(cls, quantidade: int) -> dict:
        return TelaEditarProdutoQuantidade.tela(quantidade)

    @classmethod
    def tela_editar_produto_confirmacao(cls) -> dict:
        return TelaEditarProdutoConfirmacao.tela()

    @classmethod
    def tela_editar_produto_descartar(cls) -> dict:
        return TelaEditarProdutoDescartar.tela()

    @classmethod
    def tela_editar_produto_sucesso(cls) -> None:
        TelaEditarProdutoSucesso.tela()

    @classmethod
    def tela_editar_produto_erro_nome(cls) -> None:
        TelaEditarProdutoErroNome.tela()

    @classmethod
    def tela_editar_produto_erro_preco(cls) -> None:
        TelaEditarProdutoErroPreco.tela()

    @classmethod
    def tela_editar_produto_erro_quantidade(cls) -> None:
        TelaEditarProdutoErroQuantidade.tela()

    # * Excluir produto

    @classmethod
    def tela_excluir_produto(cls) -> dict:
        return TelaExcluirProduto.tela()

    @classmethod
    def tela_excluir_produto_sucesso(cls) -> None:
        TelaExcluirProdutoSucesso.tela()

    # * Listar produtos

    @classmethod
    def tela_listar_produtos(cls, informacoes: dict) -> dict:
        return TelaListarProdutos.tela(informacoes)

    @classmethod
    def tela_pesquisar_produto(cls) -> dict:
        return TelaPesquisarProduto.tela()

    @classmethod
    def tela_visualizar_produto(cls, produto) -> dict:
        return TelaVisualizarProduto.tela(produto)
