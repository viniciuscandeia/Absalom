from .template_tela import TemplateTela

# O "_Administrador" indica que é uma tela para o Administrador


class TelaAdicionarUsuarios_Administrador(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Escolha o tipo de usuário --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Adicionar Administrador \n2 - Adicionar Gerente \n3 - Adicionar Vendedor \n4 - Voltar \n"
        )
        print(mensagem)


class TelaAdicionarUsuarios_Gerente(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Escolha o tipo de usuário --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Adicionar Gerente \n2 - Adicionar Vendedor \n3 - Voltar \n"
        print(mensagem)


class TelaAdicionarAdministrador(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Adicionar Administrador --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {
            "nome": cls._coletar_entrada("Nome: "),
            "username": cls._coletar_entrada("Username: "),
            "email": cls._coletar_entrada("Email: "),
            "senha": cls._coletar_entrada("Senha: "),
        }


class TelaAdicionarGerente(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Adicionar Gerente --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {
            "nome": cls._coletar_entrada("Nome: "),
            "username": cls._coletar_entrada("Username: "),
            "email": cls._coletar_entrada("Email: "),
            "senha": cls._coletar_entrada("Senha: "),
        }


class TelaAdicionarVendedor(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Adicionar Vendedor --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {
            "nome": cls._coletar_entrada("Nome: "),
            "username": cls._coletar_entrada("Username: "),
            "email": cls._coletar_entrada("Email: "),
            "senha": cls._coletar_entrada("Senha: "),
        }


class TelaAdicionarSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Usuário adicionado com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarErroUsername(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao adicionar usuário! O 'username' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarErroEmail(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao adicionar usuário! O 'email' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarErroSenha(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao adicionar usuário! A 'senha' deve atender as condições. --- \n"
        )

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Tamanho mínimo: 8 caracteres. \n2 - Tamanho máximo: 128 caracteres. \n3 - Deve conter, pelo menos, uma letra maiúscula. \n4 - Deve conter, pelo menos, uma letra minúscula. \n5 - Deve conter, pelo menos, um número. \n6 - Deve conter, pelo menos, um caractere especial. \n"
        )
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
