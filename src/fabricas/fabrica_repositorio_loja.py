from src.fabricas.fabrica_repositorio import FabricaRepositorio
from src.repositorios.estrategias.estrategias_gerenciamento_loja import GerenciamentoLojaRAM, GerenciamentoLojaDB
from src.repositorios.estrategias.gerenciador_repositorio_loja import GerenciadorRepositorioLoja
from src.repositorios.repositorios_lojas import RepositorioLojasRAM, RepositorioLojasDB


class FabricaRepositoriosLojas(FabricaRepositorio):
    _repositorios = {
        'ram': RepositorioLojasRAM,
        'db': RepositorioLojasDB
    }

    @staticmethod
    def criar_repositorio(tipo: str):
        repositorio_class = FabricaRepositoriosLojas._repositorios.get(
            tipo)
        if repositorio_class:
            return repositorio_class().pegar_repositorio()
        else:
            raise ValueError(f"Tipo de repositório desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Repositórios de Lojas"



class FabricaGerenciadorRepositorioLoja:
    _repositorios = {
        'ram': GerenciadorRepositorioLoja(GerenciamentoLojaRAM(RepositorioLojasRAM().pegar_repositorio())),
        'db': GerenciadorRepositorioLoja(GerenciamentoLojaDB(RepositorioLojasDB().pegar_repositorio()))
    }

    @staticmethod
    def criar_gerenciador(tipo: str):
        gerenciador = FabricaGerenciadorRepositorioLoja._repositorios.get(
            tipo)
        if gerenciador:
            return gerenciador
        else:
            raise ValueError(f"Tipo de persistência desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Gerenciadores de Repositórios das Lojas"
