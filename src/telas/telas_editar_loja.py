from .template_tela import TemplateTela


class TelaEditarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Loja --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict):
        mensagem: str = (
            f"ID: {informacoes['id']} \nNome: {informacoes['nome']} \nEndereço: {informacoes['endereco']} \n"
        )
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Editar Nome \n2 - Editar Endereço \n3 - Confirmar edição \n4 - Descartar edição \n5 - Voltar \n"
        )
        print(mensagem)


class TelaEditarLojaNome(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Nome --- \n")

    @classmethod
    def _listar_informacoes(cls, nome: str):
        print(f"Nome atual: {nome}")

    @classmethod
    def _menu(cls):
        mensagem: str = "Aviso: Deixe em branco caso não queira editar. \n"
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"nome": cls._coletar_entrada("Novo nome: ")}


class TelaEditarLojaEndereco(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Endereço --- \n")

    @classmethod
    def _listar_informacoes(cls, endereco: str):
        print(f"Endereço atual: {endereco}")

    @classmethod
    def _menu(cls):
        mensagem: str = "Aviso: Deixe em branco caso não queira editar. \n"
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"endereco": cls._coletar_entrada("Novo endereço: ")}


class TelaEditarLojaConfirmacao(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Confirmar edição? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Confirmar \n2 - Voltar \n"
        print(mensagem)


class TelaEditarLojaDescartar(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Descartar edição? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Descartar \n2 - Voltar \n"
        print(mensagem)


class TelaEditarLojaSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Loja editada com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaEditarLojaErroNome(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao editar loja! O 'nome' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaEditarLojaErroEndereco(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao editar loja! O 'endereço' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
