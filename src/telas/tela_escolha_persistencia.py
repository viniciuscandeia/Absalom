from .template_tela import TemplateTela


class TelaEscolhaPersistencia(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Escolha a persistência que será utilizada --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - RAM \n2 - DB \n"
        print(mensagem)
