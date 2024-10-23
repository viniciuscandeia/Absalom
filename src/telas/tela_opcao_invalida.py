from .template_tela import TemplateTela

class TelaOpcaoInvalida(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Opção digitada inválida. --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        pass
