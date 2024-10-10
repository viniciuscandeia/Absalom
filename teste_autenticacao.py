from src.services.autenticacao_usuario import AutenticacaoUsuario
from src.views.estados.gerenciador_telas import GerenciadorTelas
from src.views.estados.view_login import TelaLogin
from src.entidades.entidades_usuarios import Usuario
from src.fabricas.fabrica_entidades_usuarios import FabricaEntidadesUsuarios

from src.fabricas.fabrica_repositorios_usuarios import FabricaGerenciadorRepositorioUsuarios

if __name__ == '__main__':
    gerenciador_telas = GerenciadorTelas(TelaLogin())
    retorno = gerenciador_telas.exibir_tela()

    gerenciador = FabricaGerenciadorRepositorioUsuarios.criar_gerenciador(retorno)
    print(gerenciador)

    dados: dict = {
        'id': 4,
        'nome': 'Vinicius',
        'username': 'viniciuscandeia',
        'email': 'viniciuscandeia12@gmail.com',
        'senha': '0000',
        'tipo': 'gerente',
        'id_loja': 1
    }
    entidade: Usuario = FabricaEntidadesUsuarios.criar_entidade(
        'gerente', dados)
    gerenciador.adicionar(entidade.id_, entidade)


    autenticador = AutenticacaoUsuario(gerenciador)
    autenticador.autenticar(retorno['username'], retorno['senha'])

    print(autenticador.usuario_autenticado())