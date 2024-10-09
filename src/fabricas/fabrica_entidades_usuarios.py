from ..entidades.entidades_usuarios import Usuario


class FabricaEntidadesUsuarios:
    _entidades: dict = {
        'administrador': lambda dados: Usuario(dados['id'], dados['nome'], dados['username'], dados['email'], dados['senha'], 'administrador', -1),
        'gerente': lambda dados: Usuario(dados['id'], dados['nome'], dados['username'], dados['email'], dados['senha'], 'gerente', dados['id_loja']),
        'vendedor': lambda dados: Usuario(dados['id'], dados['nome'], dados['username'], dados['email'], dados['senha'], 'vendedor', dados['id_loja']),
    }

    @staticmethod
    def criar_entidade(tipo: str, dados: dict) -> Usuario:
        entidade_func = FabricaEntidadesUsuarios._entidades.get(tipo)
        if entidade_func:
            # Chama a função lambda passando os dados
            return entidade_func(dados)
        else:
            raise ValueError(f"Tipo de entidade desconhecido: {tipo}")
