import re


class ValidadorInformacoes:

    @classmethod
    # Para usuário
    def validacao_username(cls, repositorio: dict, username: str) -> bool:
        for item in repositorio:
            if repositorio[item].username == username:
                return False
        return True

    @classmethod
    def validacao_email(cls, repositorio: dict, email: str) -> bool:
        for item in repositorio:
            if repositorio[item].username == email:
                return False
        return True

    @classmethod
    def validacao_senha(cls, senha: str) -> bool:
        # Verifica tamanho mínimo e máximo
        if not (8 <= len(senha) <= 128):
            return False
        # Verifica se contém pelo menos uma letra maiúscula
        if not re.search(r"[A-Z]", senha):
            return False
        # Verifica se contém pelo menos uma letra minúscula
        if not re.search(r"[a-z]", senha):
            return False
        # Verifica se contém pelo menos um número
        if not re.search(r"[0-9]", senha):
            return False
        # Verifica se contém pelo menos um caractere especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            return False

        # Se todas as verificações passarem, a senha é válida
        return True

    @classmethod
    def validacao_nome_loja(cls, repositorio: dict, nome: str) -> bool:
        for item in repositorio:
            if repositorio[item].nome == nome:
                return False
        return True

    @classmethod
    def validacao_endereco(cls, repositorio: dict, endereco: str) -> bool:
        for item in repositorio:
            if repositorio[item].endereco == endereco:
                return False
        return True

    @classmethod
    def validacao_produto(cls, produto) -> bool:
        # Verificar se todos os campos obrigatórios estão preenchidos
        if not produto.nome or not produto.descricao:
            print("Erro: Nome ou descrição do produto não podem estar vazios.")
            return False

        # Verificar se o preço é um número válido e positivo
        if not isinstance(produto.preco, (int, float)) or produto.preco <= 0:
            print("Erro: Preço deve ser um número positivo.")
            return False

        # Verificar se a quantidade é um número inteiro positivo
        if not isinstance(produto.quantidade, int) or produto.quantidade < 0:
            print("Erro: Quantidade deve ser um número inteiro não negativo.")
            return False

        # Se todas as verificações passarem, o produto é válido
        return True
