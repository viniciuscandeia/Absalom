from ..entidades.entidades_usuarios import Usuario


class FabricaEntidadesUsuarios:
    _entidades: dict = {
        'administrador': lambda dados: Usuario(
            nome=dados['nome'],
            username=dados['username'],
            email=dados['email'],
            senha=dados['senha'],
            tipo='administrador',
            id_loja=dados['id_loja']),
        'gerente': lambda dados:  Usuario(
            nome=dados['nome'],
            username=dados['username'],
            email=dados['email'],
            senha=dados['senha'],
            tipo='gerente',
            id_loja=dados['id_loja']),
        'vendedor': lambda dados: Usuario(
            nome=dados['nome'],
            username=dados['username'],
            email=dados['email'],
            senha=dados['senha'],
            tipo='vendedor',
            id_loja=dados['id_loja']),
    }

    @staticmethod
    def criar_entidade(tipo: str, dados: dict) -> Usuario:
        entidade_func = FabricaEntidadesUsuarios._entidades.get(tipo)
        if entidade_func:
            # Chama a função lambda passando os dados
            return entidade_func(dados)
        else:
            raise ValueError(f"Tipo de entidade desconhecido: {tipo}")
