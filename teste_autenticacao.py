from src.services.autenticacao_usuario import AutenticacaoUsuario
from src.views.estados.gerenciador_telas import GerenciadorTelas
from src.views.estados.view_login import TelaLogin
from src.fabricas.fabrica_repositorios_usuarios import FabricaRepositoriosUsuarios
from src.repositorios.estrategias.gerenciador_repositorio_usuarios import GerenciadorRepositorioUsuarios
from src.repositorios.estrategias.estrategias_gerenciamento_usuarios import GerenciamentoUsuariosRAM, GerenciamentoUsuariosDB

if __name__ == '__main__':
    gerenciador_telas = GerenciadorTelas(TelaLogin())
    retorno = gerenciador_telas.exibir_tela()

    repositorio = FabricaRepositoriosUsuarios.criar_repositorio('db')
    gerenciador = GerenciadorRepositorioUsuarios(
        GerenciamentoUsuariosDB(repositorio))

    # gerenciador = GerenciadorRepositorioUsuarios(GerenciamentoUsuariosDB(repositorio))
    # repositorio = FabricaRepositoriosUsuarios.criar_repositorio('db')

    autenticador = AutenticacaoUsuario(GerenciamentoUsuariosDB(repositorio))
    autenticador.autenticar(retorno['username'], retorno['senha'])

    print(autenticador.usuario_autenticado())