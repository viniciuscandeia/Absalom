from .template_tela import TemplateTela


class TelaAssociarLojaInicial(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Associar com Loja ---")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Criar nova loja \n2 - Associar com loja existente \n"
        print(mensagem)


class TelaAssociarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Associar com Loja Existente ---")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict = None):
        for item in informacoes:
            print(informacoes[item])


class TelaAdicionarLoja(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Adicionar Loja ---")

    @classmethod
    def _coletar_informacoes(cls):
        return {
            "nome": cls._coletar_entrada("Nome: "),
            "endereco": cls._coletar_entrada("Endereço: "),
        }


class TelaAdicionarLojaSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Loja adicionada com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarLojaErroNome(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Erro ao adicionar loja! O 'nome' digitado já foi cadastrado no sistema. --- \n"
              )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarLojaErroEndereco(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Erro ao adicionar loja! O 'endereço' digitado já foi cadastrado no sistema. --- \n"
              )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
