from .template_tela import TemplateTela


class TelaExcluirVenda(TemplateTela):
    @classmethod
    def _titulo(cls):
        print("--- Excluir Venda? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Excluir \n2 - Voltar \n"
        print(mensagem)


class TelaExcluirVendaSucesso(TemplateTela):
    @classmethod
    def _titulo(cls):
        print("--- Venda excluída com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
