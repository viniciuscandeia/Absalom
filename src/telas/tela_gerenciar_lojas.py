from .template_tela import TemplateTela


class TelaGerenciarLojas(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Gerenciar Lojas --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Pesquisar Loja \n2 - Listar Lojas \n3 - Voltar \n"
        )
        print(mensagem)
