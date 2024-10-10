from src.views.estados.gerenciador_telas import GerenciadorTelas
from src.views.estados.view_login import TelaLogin

if __name__ == '__main__':

    # * Tela Login
    gerenciador_telas = GerenciadorTelas(TelaLogin())
    gerenciador_telas.exibir_tela()

    gerenciador_telas.proxima_tela('administrador')
    # gerenciador_telas.proxima_tela('gerente')

    # * Tela Inicial
    gerenciador_telas.exibir_tela()
    gerenciador_telas.proxima_tela('gerenciar_usuarios')
    # gerenciador_telas.proxima_tela('logout')

    # * Tela Gerenciar Usuários
    gerenciador_telas.exibir_tela()
    gerenciador_telas.proxima_tela('adicionar_usuario_tela_administrador')

    # * Tela Adicionar Usuário
    gerenciador_telas.exibir_tela()
    gerenciador_telas.proxima_tela('adicionar_administrador')

    # * Tela Adicionar Administrador
    gerenciador_telas.exibir_tela()
