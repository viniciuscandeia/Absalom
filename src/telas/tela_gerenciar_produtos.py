from .template_tela import TemplateTela


class TelaGerenciarProdutos(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Gerenciar Produtos --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Adicionar Produto \n2 - Administrar Produto \n3 - Listar Produtos \n4 - Voltar \n"
        )
        print(mensagem)
