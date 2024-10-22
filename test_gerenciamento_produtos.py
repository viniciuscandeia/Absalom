from src.entidades.entidade_loja import Loja
from src.entidades.entidade_produto import Produto
from src.fabricas.fabrica_repositorio_loja import FabricaRepositoriosLojas
from src.fabricas.fabrica_repositorio_produto import FabricaRepositorioProduto
from src.repositorios.estrategias.estrategias_gerenciamento_loja import GerenciamentoLojaRAM, GerenciamentoLojaDB
from src.repositorios.estrategias.estrategias_gerenciamento_produto import GerenciamentoProdutoDB
from src.repositorios.estrategias.gerenciador_repositorio_loja import GerenciadorRepositorioLoja
from src.repositorios.estrategias.gerenciador_repositorio_produto import GerenciadorRepositorioProduto

if __name__ == '__main__':

    # repositorio = FabricaRepositoriosLojas.criar_repositorio('ram')
    # gerenciador = GerenciadorRepositorioLoja(GerenciamentoLojaRAM(repositorio))

    repositorio = FabricaRepositorioProduto.criar_repositorio('db')
    gerenciador = GerenciadorRepositorioProduto(GerenciamentoProdutoDB(repositorio))

    dados: dict = {
        'nome': 'Teclado Gamer Warrior Blue switch',
        'id_loja': 1,
        'tipo': "TECLADO",
        'preco': 299,
        'quantidade': 32,
    }

    dados2: dict = {
        'nome': 'Mouse Gamer Warrior Blue 399 DPI',
        'id_loja': 1,
        'tipo': "MOUSE",
        'preco': 199,
        'quantidade': 3,
    }


    loja2 = Produto(nome=dados['nome'],
                    id_loja=dados['id_loja'],
                    tipo = dados['tipo'],
                    preco= dados['preco'],
                    quantidade = dados['quantidade'],
                    )


    lojaEditada = Produto(nome=dados2['nome'],
                    id_loja=dados2['id_loja'],
                    tipo = dados2['tipo'],
                    preco= dados2['preco'],
                    quantidade = dados2['quantidade'],
                    )

    # gerenciador.adicionar(entidade=loja2)
    # gerenciador.remover(3)
    # gerenciador.editar(id_=4, entidade=lojaEditada)
    lista = gerenciador.listar()
    for item in lista:
        print(item)

    item = gerenciador.buscar(4)
    print(item)


