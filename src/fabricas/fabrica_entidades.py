from ..entidades.entidade import Entidade
from ..entidades.entidade_loja import Loja
from ..entidades.entidade_notificacao import Notificacao
from ..entidades.entidade_produto import Produto
from ..entidades.entidade_venda import Venda
from ..entidades.entidades_usuarios import Usuario
from .fabrica_abstrata import FabricaAbstrata


class FabricaEntidades(FabricaAbstrata):
    _entidades: dict = {
        "administrador": lambda dados: Usuario(
            id_=dados["id"],
            nome=dados["nome"],
            username=dados["username"],
            email=dados["email"],
            senha=dados["senha"],
            tipo="administrador",
            id_loja=0,
        ),
        "gerente": lambda dados: Usuario(
            id_=dados["id"],
            nome=dados["nome"],
            username=dados["username"],
            email=dados["email"],
            senha=dados["senha"],
            tipo="gerente",
            id_loja=dados["id_loja"],
        ),
        "vendedor": lambda dados: Usuario(
            id_=dados["id"],
            nome=dados["nome"],
            username=dados["username"],
            email=dados["email"],
            senha=dados["senha"],
            tipo="vendedor",
            id_loja=dados["id_loja"],
        ),
        "loja": lambda dados: Loja(
            id_=dados["id"],
            nome=dados["nome"],
            endereco=dados["endereco"],
        ),
        "produto": lambda dados: Produto(
            id_=dados["id"],
            nome=dados["nome"],
            descricao=dados["descricao"],
            preco=dados["preco"],
            quantidade=dados["quantidade"],
            id_loja=dados["id_loja"],
        ),
        "notificacao": lambda dados: Notificacao(
            id_=dados["id"],
            mensagem=dados["mensagem"],
            from_user_id=dados["from_user_id"],
            to_loja_id=dados["to_loja_id"],
        ),
        "venda": lambda dados: Venda(
            id_=dados["id"],
            id_produto=dados["id_produto"],
            id_vendedor=dados["id_vendedor"],
            id_loja=dados["id_loja"],
            quantidade=dados["quantidade"],
            preco_total=dados["preco_total"],
        ),
    }

    def criar(self, tipo: str, dados: dict) -> Entidade:
        entidade_func = FabricaEntidades._entidades.get(tipo)
        return entidade_func(dados)
