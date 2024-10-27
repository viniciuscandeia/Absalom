from .template_tela import TemplateTela

class TelaRelatorios(TemplateTela):
    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Relatorio em HTML \n2 - Relatorio em PDF  \n3 - Voltar"
        )
        print(mensagem)
