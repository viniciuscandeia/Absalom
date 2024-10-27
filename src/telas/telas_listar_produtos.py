from ..entidades.entidade_produto import Produto
from .template_tela import TemplateTela


class TelaListarProdutos(TemplateTela):

    @classmethod
    def _titulo(cls):
        pass

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        if informacoes:
            chaves: list = list(informacoes.keys())
            id_loja: int = informacoes[chaves[0]].id_loja
            print(f"--- Produtos da Loja {id_loja} --- \n")

            for item in informacoes:
                print(informacoes[item])
        else:
            print("--- Não há produtos cadastrados! ---\n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Visualizar Produto \n2 - Voltar \n"
        print(mensagem)


class TelaPesquisarProduto(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Pesquisar Produto --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id": cls._coletar_entrada("ID: ")}


class TelaVisualizarProduto(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Informações do Produto --- \n")

    @classmethod
    def _listar_informacoes(cls, produto: Produto):
        mensagem: str = (
            f"ID: {produto.id_} \nNome: {produto.nome} \nDescrição: {produto.descricao} \nPreço (R$): {produto.preco} \nQuantidade: {produto.quantidade} \n"
        )
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Editar Produto \n2 - Excluir Produto \n3 - Voltar \n"
        print(mensagem)
