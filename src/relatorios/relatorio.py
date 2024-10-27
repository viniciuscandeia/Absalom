import datetime
from abc import ABC, abstractmethod

from src.execoes.RelatorioError import RelatorioError
from src.repositorios.gerenciadores.gerenciador_usuarios import GerenciadorUsuarios


class Relatorio(ABC):
    def __init__(self, gerenciador_usuarios: GerenciadorUsuarios):
        self.gerenciador_usuarios = gerenciador_usuarios
        self.total_adm = 0
        self.total_gerente = 0
        self.total_vendedor = 0
        self.total_usuarios = 0

    def get_total_adm(self)->int:
        map_adm = self.gerenciador_usuarios.listar('administrador')

        return len(map_adm)

    def get_total_gerente(self) -> int:
        map_adm = self.gerenciador_usuarios.listar('gerente')

        return len(map_adm)

    def get_total_vendedor(self) -> int:
        map_adm = self.gerenciador_usuarios.listar('vendedor')

        return len(map_adm)

    def get_total_usuarios(self) -> int:
        quantity_adm = self.get_total_adm()
        quantity_gerente = self.get_total_gerente()
        quantity_vendedor = self.get_total_vendedor()
        quantity_usuarios = quantity_adm + quantity_gerente + quantity_vendedor

        self.total_adm = quantity_adm
        self.total_gerente = quantity_gerente
        self.total_vendedor = quantity_vendedor
        self.total_usuarios = quantity_usuarios

        return quantity_usuarios

    def get_porcentagem_adms(self):
        quantidade_adm = self.get_total_adm()
        return (quantidade_adm / self.total_usuarios) * 100

    def get_porcentagem_gerente(self):
        quantidade_gerente = self.get_total_gerente()
        return (quantidade_gerente / self.total_usuarios) * 100

    def get_porcentagem_vendedor(self):
        quantidade_vendedor = self.get_total_vendedor()
        return (quantidade_vendedor / self.total_usuarios) * 100

    def gerar_nome_arquivo(self):
        data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return data_atual

    @abstractmethod
    def formatar_relatorio(self, data: dict):
        pass

    #template method
    def gerar_relatorio(self):
        try:
            total = self.get_total_usuarios()
            porcentagem_adm = self.get_porcentagem_adms()
            porcentagem_gerente = self.get_porcentagem_gerente()
            porcentagem_vendedore = self.get_porcentagem_vendedor()
            quantidade_gerente = self.get_total_gerente()
            quantidade_adm = self.get_total_adm()
            quantidade_vendedor = self.get_total_vendedor()

            data_relatorio = {'total': total,
                              'quantidade_adm': quantidade_adm,
                              'quantidade_gerente': quantidade_gerente,
                              'quantidade_vendedor': quantidade_vendedor,
                              'porcentagemVendedores': porcentagem_vendedore,
                              'porcentagemAdm': porcentagem_adm,
                              'porcentagemGerente': porcentagem_gerente,
                              }
            self.formatar_relatorio(data=data_relatorio)
            return True
        except Exception:
            return False

