from abc import ABC, abstractmethod


class EstadoTela(ABC):
    def __init__(self):
        self.contexto = None

    def definir_contexto(self, contexto):
        self.contexto = contexto

    def atualizar_estado(self, opcao: str, transicoes: dict):
        if opcao in transicoes:
            proximo_estado = transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    @abstractmethod
    def exibir(self):
        pass

    @abstractmethod
    def proxima_tela(self, opcao: str):
        pass

    @abstractmethod
    def tela_anterior(self, opcao: str):
        pass

    @abstractmethod
    def preparar_dados_recebidos(self, dados: list):
        pass
