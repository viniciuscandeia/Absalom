class TemplateTela:

    @classmethod
    def tela(cls, informacoes: dict = None) -> dict:
        cls._titulo()
        cls._listar_informacoes(informacoes)
        cls._menu()
        return cls._coletar_informacoes()

    @classmethod
    def _titulo(cls):
        pass

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        pass

    @classmethod
    def _menu(cls):
        pass

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"opcao": cls._coletar_entrada("Opção: ")}

    @classmethod
    def _coletar_entrada(cls, prompt: str) -> str:
        return input(prompt)
