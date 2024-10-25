from .template_tela import TemplateTela

class TelaExcluirLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Excluir Loja? --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = ('1 - Excluir \n2 - Voltar \n')
        print(mensagem)

class TelaExcluirLojaSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Loja excluída com sucesso! --- \n')

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
