from abc import ABC, abstractmethod


class EstadoTela(ABC):
    def __init__(self):
        self.contexto = None

    def definir_contexto(self, contexto):
        self.contexto = contexto

    @abstractmethod
    def exibir(self):
        pass

    @abstractmethod
    def proxima_tela(self, opcao: str):
        pass

    @abstractmethod
    def preparar_dados_recebidos(self, dados: list):
        pass
