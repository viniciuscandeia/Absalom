from ..command.command_adicionar_loja import AdicionarLojaCommand
from ..command.command_excluir_loja import ExcluirLojaCommand
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
        mensagem: str = "1 - Escolher Loja \n2 - Voltar \n"
        print(mensagem)


class TelaListarLojasFluxoFiltro(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Listar Lojas --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        for item in informacoes:
            print(informacoes[item])

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Mostrar usuários de uma loja \n2 - Voltar \n"
        print(mensagem)


class TelaPesquisarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Pesquisar Loja --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id": cls._coletar_entrada("ID: ")}


# class TelaVisualizarLoja(TemplateTela):
#
#     @classmethod
#     def _titulo(cls):
#         print("--- Informações da Loja --- \n")
#
#     @classmethod
#     def _listar_informacoes(cls, loja: Loja):
#         mensagem: str = (
#             f"ID: {loja.id_} \nNome: {loja.nome} \nEndereco: {loja.endereco} \n"
#         )
#         print(mensagem)
#
#     @classmethod
#     def _menu(cls):
#         mensagem: str = (
#             "1 - Gerenciar Funcionários \n2 - Gerenciar Produtos \n3 - Editar Loja \n4 - Excluir Loja \n5 - Voltar \n"
#         )
#         print(mensagem)

class TelaVisualizarLoja(TemplateTela):
    def __init__(self, invoker, gerenciador_lojas):
        self.invoker = invoker
        self.gerenciador_lojas = gerenciador_lojas

    @classmethod
    def _titulo(cls):
        print("--- Informações da Loja --- \n")

    @classmethod
    def _listar_informacoes(cls, loja: Loja):
        mensagem: str = (
            f"ID: {loja.id_} \nNome: {loja.nome} \nEndereco: {loja.endereco} \n"
        )
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Editar Loja \n2 - Excluir Loja \n3 - Voltar"
        print(mensagem)

    def excluir_loja(self, loja):
        command = ExcluirLojaCommand(self.gerenciador_lojas, loja)
        self.invoker.execute_command(command)

    def adicionar_loja(self, loja):
        command = AdicionarLojaCommand(self.gerenciador_lojas, loja)
        self.invoker.execute_command(command)
