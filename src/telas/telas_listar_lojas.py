from ..entidades.entidade_loja import Loja
from .template_tela import TemplateTela


class TelaFiltrarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Filtrar por Loja --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Listar Lojas \n2 - Pesquisar Loja \n3 - Voltar \n"
        print(mensagem)


class TelaListarLojas(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar Lojas --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        for item in informacoes:
            print(informacoes[item])

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Visualizar Loja \n2 - Voltar \n"
        print(mensagem)


class TelaPesquisarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Pesquisar Loja --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id": cls._coletar_entrada("ID: ")}


class TelaVisualizarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Visualizar Loja --- \n")

    @classmethod
    def _listar_informacoes(cls, loja: Loja):
        mensagem: str = (f"ID: {loja.id_} \nNome: {loja.nome} \nEndereco: {loja.endereco} \n")
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Editar Loja \n2 - Excluir Loja \n3 - Voltar"
        print(mensagem)
