from .template_tela import TemplateTela


class TelaGerenciarVendas(TemplateTela):
    @classmethod
    def _titulo(cls):
        print("--- Gerenciar Vendas --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Realizar Venda \n2 - Listar Vendas \n3 - Voltar \n"
        )
        print(mensagem)
