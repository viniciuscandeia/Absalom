from .template_tela import TemplateTela


class TelaGerenciarUsuarios(TemplateTela):

    @classmethod
    def _titulo(cls):
        print('--- Gerenciar Usuários --- \n')

    @classmethod
    def _menu(cls):
        mensagem: str = (
            "1 - Adicionar Usuário \n2 - Administrar Usuário \n3 - Listar Usuários \n4 - Voltar \n"
        )
        print(mensagem)
