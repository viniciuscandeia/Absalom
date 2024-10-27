from .template_tela import TemplateTela


class TelaListarVendas(TemplateTela):

    @classmethod
    def _titulo(cls):
        pass

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        chaves: list = list(informacoes.keys())
        id_loja: int = informacoes[chaves[0]].id_loja
        print(f"--- Vendas da Loja {id_loja} --- \n")

        for item in informacoes:
            print(informacoes[item])

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        pass


class TelaPesquisarVenda(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Pesquisar Venda --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id": cls._coletar_entrada("ID: ")}
