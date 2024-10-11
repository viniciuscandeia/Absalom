from .view_estado_tela import EstadoTela

class GerenciadorTelas:
    def __init__(self, estado_inicial: EstadoTela):
        self.estado_atual: EstadoTela = estado_inicial
        self.estado_atual.definir_contexto(self)

    def trocar_estado(self, novo_estado: EstadoTela):
        self.estado_atual = novo_estado
        self.estado_atual.definir_contexto(self)

    def exibir_tela(self):
        return self.estado_atual.exibir()

    def proxima_tela(self, opcao: str):
        self.estado_atual.proxima_tela(opcao)

    def enviar_conteudo(self, dados: list):
        self.estado_atual.preparar_dados_recebidos(dados)