from src.fabricas.fabrica_repositorio import FabricaRepositorio
from src.repositorios.estrategias.estrategias_lojas import EstrategiaLojasRAM, EstrategiaLojasDB
from src.repositorios.gerenciadores.gerenciador_lojas import GerenciadorLojas
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



class FabricaGerenciadorLojas:
    _repositorios = {
        'ram': GerenciadorLojas(EstrategiaLojasRAM(RepositorioLojasRAM().pegar_repositorio())),
        'db': GerenciadorLojas(EstrategiaLojasDB(RepositorioLojasDB().pegar_repositorio()))
    }

    @staticmethod
    def criar_gerenciador(tipo: str):
        gerenciador = FabricaGerenciadorLojas._repositorios.get(
            tipo)
        if gerenciador:
            return gerenciador
        else:
            raise ValueError(f"Tipo de persistência desconhecido: {tipo}")

    def __str__(self):
        return "Fábrica dos Gerenciadores de Repositórios das Lojas"
