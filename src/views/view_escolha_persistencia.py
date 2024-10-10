
class TelaEscolhaPersistencia:

    @staticmethod
    def exibir():
        mensagem: str = """
        --- Escolha a persistência que será utilizada ---
        1 - RAM
        2 - DB
        """
        print(mensagem)
        opcao = input('Opção: ')
        return opcao

    @staticmethod
    def pegar_persistencia():
        retorno: str = ''
        while retorno != '1' and retorno != '2':
            retorno = TelaEscolhaPersistencia.exibir()

        if retorno == '1':
            return 'ram'
        else:
            return 'db'
