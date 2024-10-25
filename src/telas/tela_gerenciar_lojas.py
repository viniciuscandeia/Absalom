from .template_tela import TemplateTela


class TelaGerenciarLojas(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Gerenciar Lojas --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Listar Lojas \n2 - Pesquisar Loja \n3 - Voltar \n"
        )
        print(mensagem)
