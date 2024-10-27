from .template_tela import TemplateTela


class TelaRelatorios(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Emitir Relatório --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Relatório em HTML \n2 - Relatório em PDF  \n3 - Voltar \n"
        print(mensagem)


class TelaRelatoriosPDFSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Relatório em PDF criado com sucesso na raiz! --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        pass


class TelaRelatoriosHTMLSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Relatório em HTML criado com sucesso na raiz! --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        pass


class TelaRelatoriosErro(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Erro ao emitir relatório! --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        pass
