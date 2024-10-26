from .template_tela import TemplateTela


class TelaAdicionarProdutos(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Adicionar Produto --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {
            "nome": cls._coletar_entrada("Nome: "),
            "descricao": cls._coletar_entrada("Descrição: "),
            "preco": cls._coletar_entrada("Preço (R$): "),
            "quantidade": cls._coletar_entrada("Quantidade: "),
        }


class TelaAdicionarProdutoSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Produto adicionado com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarProdutoErroNome(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao adicionar produto! O 'nome' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarProdutoErroDescricao(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao adicionar produto! A 'descrição' não pode ficar vazia. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarProdutoErroPreco(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Erro ao adicionar produto! O 'preço' digitado não é válido. --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaAdicionarProdutoErroQuantidade(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao adicionar usuário! A 'quantidade' digitada não é válida. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
