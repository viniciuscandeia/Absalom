from src.entidades.entidade_loja import Loja
from src.fabricas.fabrica_repositorio_loja import FabricaRepositoriosLojas
from src.repositorios.estrategias.estrategias_gerenciamento_loja import GerenciamentoLojaRAM, GerenciamentoLojaDB
from src.repositorios.estrategias.gerenciador_repositorio_loja import GerenciadorRepositorioLoja

if __name__ == '__main__':

    # repositorio = FabricaRepositoriosLojas.criar_repositorio('ram')
    # gerenciador = GerenciadorRepositorioLoja(GerenciamentoLojaRAM(repositorio))

    repositorio = FabricaRepositoriosLojas.criar_repositorio('db')
    gerenciador = GerenciadorRepositorioLoja(GerenciamentoLojaDB(repositorio))

    dados: dict = {
        'nome': 'Magazine',
        'endereco': 'Rua Felizardo Leite, 561',
    }

    dados2: dict = {
        'nome': 'Magazine Editada',
        'endereco': 'Rua Felizardo Leite, 5612222',
    }

    loja = Loja(nome=dados.get('nome'),
                endereco=dados.get('endereco'))

    loja2 = Loja(nome=dados2.get('nome'),
                endereco=dados2.get('endereco'))

    gerenciador.adicionar(entidade=loja)
    gerenciador.adicionar(entidade=loja2)
    # gerenciador.editar(4, entidade= loja2)

    lista = gerenciador.buscar(2)

    for item in lista:
        print(item)