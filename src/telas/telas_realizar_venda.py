from .template_tela import TemplateTela


class TelaInicialVenda(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Realizar Venda --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - ID do produto \n2 - Quantidade do produto \n3 - Finalizar Venda \n4 - Cancelar Venda \n"
        )
        print(mensagem)


class TelaDefinirIDProdutoVenda(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Realizar Venda --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id": cls._coletar_entrada("Informe o ID do Produto: ")}
    
class TelaDefinirQuantidadeVenda(TemplateTela):

    @classmethod
    def _titulo(cls):
        print("--- Realizar Venda --- \n")

    @classmethod
    def _coletar_informacoes(cls) -> dict:
        return {"id": cls._coletar_entrada("Informe a quantidade do produto: ")}


class TelaFinalizarVenda(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Finalizar Venda --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Confirmar \n2 - Voltar \n3 - Finalizar Venda "
        )
        print(mensagem)


class TelaVendaFinalizada(TemplateTela):
    @classmethod
    def _titulo(cls):
        print('--- Venda finalizada com sucesso! --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "\nAperte qualquer tecla para voltar ao Menu"
        )
        print(mensagem)