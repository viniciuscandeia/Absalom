from .template_tela import TemplateTela


class TelaExcluirProduto(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Excluir Produto? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Excluir \n2 - Voltar \n"
        print(mensagem)


class TelaExcluirProdutoSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Produto excluído com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
