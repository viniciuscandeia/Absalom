from src.fabricas.fabrica_repositorios_usuarios import FabricaRepositoriosUsuarios
from src.repositorios.estrategias.gerenciador_repositorio_usuarios import GerenciadorRepositorioUsuarios
from src.repositorios.estrategias.estrategias_gerenciamento_usuarios import GerenciamentoUsuariosRAM, GerenciamentoUsuariosDB
from src.entidades.entidades_usuarios import Usuario
from src.fabricas.fabrica_entidades_usuarios import FabricaEntidadesUsuarios


if __name__ == '__main__':

    # repositorio = FabricaRepositoriosUsuarios.criar_repositorio('ram')
    # gerenciador = GerenciadorRepositorioUsuarios(GerenciamentoUsuariosRAM(repositorio))

    repositorio = FabricaRepositoriosUsuarios.criar_repositorio('db')
    gerenciador = GerenciadorRepositorioUsuarios(GerenciamentoUsuariosDB(repositorio))

    dados: dict = {
        'id': 1,
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

    lista = gerenciador.listar(tipo=None, id_loja=None)
    for item in lista:
        print(item)

    # entidade_buscada: Usuario = gerenciador.buscar(1)
    # print(f'Busca 1: {entidade_buscada}')

    # gerenciador.remover(1)

    # lista = gerenciador.listar(tipo=None, id_loja=1)
    # for item in lista:
    #     print(item)
