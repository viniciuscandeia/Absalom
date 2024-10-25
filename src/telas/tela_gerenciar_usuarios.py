from .template_tela import TemplateTela


class TelaGerenciarUsuarios(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Gerenciar Usuários --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Listar Usuários \n2 - Pesquisar Usuário \n3 - Adicionar Usuário \n4 - Voltar \n"
        )
        print(mensagem)
