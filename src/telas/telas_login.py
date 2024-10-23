from .template_tela import TemplateTela


class TelaLogin(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Login --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {
            "username": cls._coletar_entrada("Username: "),
            "senha": cls._coletar_entrada("Senha: "),
        }


class TelaLoginErro(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Erro ao realizar login! Username/senha inválido(s). --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        pass
