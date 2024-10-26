from src.fabricas.fabrica_repositorio import FabricaRepositorio
from src.repositorios.repositorio_produto import RepositorioProdutoRAM, RepositorioProdutoDB
from src.repositorios.gerenciadores.gerenciador_produtos import GerenciadorProdutos
from src.repositorios.estrategias.estrategias_produtos import EstrategiaProdutosRAM, EstrategiaProdutosDB


class FabricaRepositorioProduto(FabricaRepositorio):
    _repositorios = {
        'ram': RepositorioProdutoRAM,
        'db': RepositorioProdutoDB
    }

    @staticmethod
    def criar_repositorio(tipo: str):
        repositorio_class = FabricaRepositorioProduto._repositorios.get(
            tipo)
        if repositorio_class:
            return repositorio_class().pegar_repositorio()
        else:
            raise ValueError(f"Tipo de repositório desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Repositórios de Produto"

class FabricaGerenciadorProdutos:
    _repositorios = {
        'ram': GerenciadorProdutos(EstrategiaProdutosRAM(RepositorioProdutoRAM().pegar_repositorio())),
        'db': GerenciadorProdutos(EstrategiaProdutosDB(RepositorioProdutoDB().pegar_repositorio()))
    }

    @staticmethod
    def criar_gerenciador(tipo: str):
        gerenciador = FabricaGerenciadorProdutos._repositorios.get(
            tipo)
        if gerenciador:
            return gerenciador
        else:
            raise ValueError(f"Tipo de persistência desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Gerenciadores de Repositórios dos produtos"