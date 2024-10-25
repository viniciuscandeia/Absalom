from .template_tela import TemplateTela

class TelaExcluirUsuario(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Excluir Usuário? --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = ('1 - Excluir \n2 - Voltar \n')
        print(mensagem)

class TelaExcluirUsuarioSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Usuário excluido com sucesso! --- \n')

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
