from .template_tela import TemplateTela


class TelaEditarUsuario(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Usuário --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict):
        mensagem: str = (
            f"ID: {informacoes['id']} \nNome: {informacoes['nome']} \nUsername: {informacoes['username']} \nEmail: {informacoes['email']} \n"
        )
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Editar Nome \n2 - Editar Username \n3 - Editar Email \n4 - Confirmar edição \n5 - Descartar edição \n6 - Voltar"
        )
        print(mensagem)


class TelaEditarUsuarioNome(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Nome --- \n")

    @classmethod
    def _listar_informacoes(cls, nome: str):
        print(f"Nome atual: {nome}")

    @classmethod
    def _menu(cls):
        mensagem: str = 'Aviso: Deixe em branco caso não queira editar.'
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"nome": cls._coletar_entrada("Novo nome: ")}


class TelaEditarUsuarioUsername(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Username --- \n")

    @classmethod
    def _listar_informacoes(cls, username: str):
        print(f"Username atual: {username}")

    @classmethod
    def _menu(cls):
        mensagem: str = 'Aviso: Deixe em branco caso não queira editar.'
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"username": cls._coletar_entrada("Novo username: ")}


class TelaEditarUsuarioEmail(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Email --- \n")

    @classmethod
    def _listar_informacoes(cls, email: str):
        print(f"Email atual: {email}")

    @classmethod
    def _menu(cls):
        mensagem: str = 'Aviso: Deixe em branco caso não queira editar.'
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"email": cls._coletar_entrada("Novo email: ")}


class TelaEditarUsuarioConfirmacao(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Confirmar edição? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Confirmar \n2 - Voltar"
        print(mensagem)


class TelaEditarUsuarioDescartar(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Descartar edição? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Descartar \n2 - Voltar"
        print(mensagem)


class TelaEditarUsuarioSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Usuário editado com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaEditarUsuarioErroUsername(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao editar usuário! O 'username' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaEditarUsuarioErroEmail(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao editar usuário! O 'email' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
