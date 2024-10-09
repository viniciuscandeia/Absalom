from src.fabricas.fabrica_repositorios_usuarios import FabricaAbstrataRepositoriosUsuarios
from src.repositorios.estrategias.estrategias_gerenciamento_usuarios import GerenciamentoAdministradoresDB, GerenciamentoUsuariosDB, GerenciamentoUsuariosRAM
from src.entidades.entidades_usuarios import Usuario
from src.repositorios.estrategias.gerenciador_repositorio import GerenciadorRepositorio

if __name__ == '__main__':
    fabrica_repositorios = FabricaAbstrataRepositoriosUsuarios.criar_fabrica(
        'db')
    print(fabrica_repositorios)

    repositorio_administradores_db = fabrica_repositorios.criar_repositorio('administradores')
    repositorio_usuarios_db = fabrica_repositorios.criar_repositorio('usuarios')

    fabrica_repositorios = FabricaAbstrataRepositoriosUsuarios.criar_fabrica('ram')

    repositorio_usuarios_ram = fabrica_repositorios.criar_repositorio('usuarios')
    repositorio_administradores_ram = fabrica_repositorios.criar_repositorio('administradores')

    print(repositorio_administradores_db)

    gerenciador_administradores_db = GerenciadorRepositorio(
        GerenciamentoAdministradoresDB(repositorio_administradores_db))
    gerenciador_usuarios_db = GerenciadorRepositorio(GerenciamentoUsuariosDB(repositorio_usuarios_db))

    usuario = Usuario(1, 'Vinicius', 'viniciuscandeia',
                      'viniciuscandeia12@gmail.com', '0000', 'gerente', 1)
    # gerenciador_usuarios_db.adicionar(usuario.id_, usuario)

    usuario = gerenciador_usuarios_db.buscar(1)
    print(usuario)