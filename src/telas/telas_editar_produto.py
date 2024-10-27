from .template_tela import TemplateTela


class TelaEditarProduto(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Produto --- \n")

    @classmethod
    def _listar_informacoes(cls, informacoes: dict):
        mensagem: str = (
            f"ID: {informacoes['id']} \nNome: {informacoes['nome']} \nDescrição: {informacoes['descricao']} \nPreço: {informacoes['preco']} \nQuantidade: {informacoes['quantidade']} \n"
        )
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Editar Nome \n2 - Editar Descrição \n3 - Editar Preço \n4 - Editar Quantidade \n5 - Confirmar edição \n6 - Descartar edição \n7 - Voltar"
        )
        print(mensagem)


class TelaEditarProdutoNome(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Nome --- \n")

    @classmethod
    def _listar_informacoes(cls, nome: str):
        print(f"Nome atual: {nome}")

    @classmethod
    def _menu(cls):
        mensagem: str = "Aviso: Deixe em branco caso não queira editar."
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"nome": cls._coletar_entrada("Novo nome: ")}


class TelaEditarProdutoDescricao(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Descrição --- \n")

    @classmethod
    def _listar_informacoes(cls, descricao: str):
        print(f"Descrição atual: {descricao}")

    @classmethod
    def _menu(cls):
        mensagem: str = "Aviso: Deixe em branco caso não queira editar."
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"descricao": cls._coletar_entrada("Nova descrição: ")}


class TelaEditarProdutoPreco(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Preço --- \n")

    @classmethod
    def _listar_informacoes(cls, preco: float):
        print(f"Preço atual (R$): {preco}")

    @classmethod
    def _menu(cls):
        mensagem: str = "Aviso: Deixe em branco caso não queira editar."
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"preco": cls._coletar_entrada("Novo preço (R$): ")}


class TelaEditarProdutoQuantidade(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Editar Quantidade --- \n")

    @classmethod
    def _listar_informacoes(cls, quantidade: int):
        print(f"Quantidade atual: {quantidade}")

    @classmethod
    def _menu(cls):
        mensagem: str = "Aviso: Deixe em branco caso não queira editar."
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"quantidade": cls._coletar_entrada("Nova quantidade: ")}


class TelaEditarProdutoConfirmacao(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Confirmar edição? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Confirmar \n2 - Voltar"
        print(mensagem)


class TelaEditarProdutoDescartar(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Descartar edição? --- \n")

    @classmethod
    def _menu(cls):
        mensagem: str = "1 - Descartar \n2 - Voltar"
        print(mensagem)


class TelaEditarProdutoSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Produto editado com sucesso! --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaEditarProdutoErroNome(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao editar produto! O 'nome' digitado já foi cadastrado no sistema. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaEditarProdutoErroPreco(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Erro ao editar produto! O 'preço' digitado não é válido. --- \n")

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass


class TelaEditarProdutoErroQuantidade(TemplateTela):

    @classmethod
    def _titulo(cls):
        print(
            "--- Erro ao editar usuário! A 'quantidade' digitada não é válida. --- \n"
        )

    @classmethod
    def _coletar_informacoes(cls, informacoes: dict = None) -> dict:
        pass
