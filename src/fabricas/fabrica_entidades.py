from ..entidades.entidade_loja import Loja
from ..entidades.entidades_usuarios import Usuario
from ..entidades.entidade import Entidade

class FabricaEntidades:
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
    }

    @staticmethod
    def criar_entidade(tipo: str, dados: dict) -> Entidade:
        entidade_func = FabricaEntidades._entidades.get(tipo)
        if entidade_func:
            # Chama a função lambda passando os dados
            return entidade_func(dados)
        else:
            raise ValueError(f"Tipo de entidade desconhecido: {tipo}")
