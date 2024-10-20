from src.fabricas.fabrica_repositorios_usuarios import FabricaRepositoriosUsuarios
from src.repositorios.criar_tabela import usuarios
from src.repositorios.estrategias.gerenciador_repositorio_usuarios import GerenciadorRepositorioUsuarios
from src.repositorios.estrategias.estrategias_gerenciamento_usuarios import GerenciamentoUsuariosRAM, GerenciamentoUsuariosDB
from src.entidades.entidades_usuarios import Usuario
from src.fabricas.fabrica_entidades_usuarios import FabricaEntidadesUsuarios


if __name__ == '__main__':

    repositorio = FabricaRepositoriosUsuarios.criar_repositorio('ram')
    gerenciador = GerenciadorRepositorioUsuarios(GerenciamentoUsuariosRAM(repositorio))

    # repositorio = FabricaRepositoriosUsuarios.criar_repositorio('db')
    # gerenciador = GerenciadorRepositorioUsuarios(GerenciamentoUsuariosDB(repositorio))

    dados: dict = {
        'nome': 'Vinicius',
        'username': 'viniciuscandeia2',
        'email': 'viniciuscandeia122@gmail.com',
        'senha': '0000',
        'tipo': 'gerente',
        'id_loja': 1
    }
    novo_usuario = FabricaEntidadesUsuarios().criar_entidade(tipo="gerente", dados=dados)
    novo_usuario2 = FabricaEntidadesUsuarios().criar_entidade(tipo="administrador", dados=dados)

    gerenciador.adicionar(entidade=novo_usuario)
    gerenciador.adicionar(entidade=novo_usuario2)

    # entidade_buscada: Usuario = gerenciador.buscar(1)
    # print(f'Busca 1: {entidade_buscada}')

    # gerenciador.remover(1)

    lista = gerenciador.listar(tipo=None)
    for item in lista:
        print(item)
