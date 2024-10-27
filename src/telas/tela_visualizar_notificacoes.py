from .template_tela import TemplateTela

class TelaVisualizarNotificacoes(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Visualizar Notificações --- \n')

    @classmethod
    def _listar_informacoes(cls, informacoes: list):
        for item in informacoes:
            print(item)

    @classmethod
    def _menu(cls):
        mensagem: str = '1 - Voltar \n'
