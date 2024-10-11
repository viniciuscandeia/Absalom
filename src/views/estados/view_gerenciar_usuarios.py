from .view_estado_tela import EstadoTela


class TelaGerenciarUsuarios(EstadoTela):
    def __init__(self):
        super().__init__()
        self.transicoes = {}

    def exibir(self):
        mensagem: str = \
            """
        --- Gerenciar Usuários ---
        1 - Adicionar Usuário
        2 - Administrar Usuário
        3 - Listar Usuários
        4 - Voltar
        """
        print(mensagem)
        opcao = input('Opção: ')
        return opcao

    def proxima_tela(self, opcao):
        from .view_telas_inicais import TelaInicialAdministrador, TelaInicialGerente
        from .view_adicionar_usuarios import TelaAdicionarUsuarios_Administrador, TelaAdicionarUsuarios_Gerente
        from .view_listar_usuarios import TelaListar_Administradores, TelaListar_Gerente

        self.transicoes = {
            'adicionar_usuario_tela_administrador': TelaAdicionarUsuarios_Administrador(),
            'adicionar_usuario_tela_gerente': TelaAdicionarUsuarios_Gerente(),
            'administrador_usuario': None,
            'listar_usuarios_tela_administrador': TelaListar_Administradores(),
            'listar_usuarios_tela_gerente': TelaListar_Gerente(),
            'voltar_administrador': TelaInicialAdministrador(),
            'voltar_gerente': TelaInicialGerente(),
        }

        if opcao in self.transicoes:
            proximo_estado = self.transicoes[opcao]
            proximo_estado.definir_contexto(self.contexto)
            self.contexto.trocar_estado(proximo_estado)

    def preparar_dados_recebidos(self, dados: list):
        pass
