from .template_tela import TemplateTela


class TelaInicialVenda(TemplateTela):
    @classmethod
    def _titulo(cls):
        print('--- Realizar Venda --- \n')

    @classmethod
    def _listar_informacoes(cls, informacoes: dict):
        mensagem: str = f'ID Produto: {informacoes['id']} \nPreço Unidade (R$): {informacoes['preco']} \nQuantidade Disponível: {informacoes['quant_disponivel']} \n\nQuantidade Desejada: {informacoes['quant_desejada']} \n '
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - ID do produto \n2 - Quantidade do produto \n3 - Finalizar Venda \n4 - Voltar \n"
        )
        print(mensagem)


class TelaDefinirIDProdutoVenda(TemplateTela):
    @classmethod
    def _titulo(cls):
        print("--- Realizar Venda --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id_produto": cls._coletar_entrada("Informe o ID do Produto: ")}


class TelaDefinirQuantidadeVenda(TemplateTela):
    @classmethod
    def _titulo(cls):
        print("--- Realizar Venda --- \n")

    @classmethod
    def _listar_informacoes(cls, quant_disponivel: int):
        mensagem: str = f'Quantidade Disponível: {quant_disponivel}'
        print(mensagem)

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"quantidade": cls._coletar_entrada("Informe a quantidade do produto: ")}


class TelaFinalizarVenda(TemplateTela):
    @classmethod
    def _titulo(cls):
        print('--- Finalizar Venda --- \n')

    @classmethod
    def _listar_informacoes(cls, informacoes: dict):
        mensagem: str = f'ID Produto: {informacoes['id']} \nPreço Total (R$): {informacoes['preco_total']} \nQuantidade: {informacoes['quant_desejada']} \n'
        print(mensagem)

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Confirmar \n2 - Voltar \n"
        )
        print(mensagem)


class TelaVendaSucesso(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Venda finalizada com sucesso! --- \n')

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        pass
