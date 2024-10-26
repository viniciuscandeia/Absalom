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
    def validacao_produto_nome_descricao(cls, texto: str) -> bool:
        if not texto:
            return False
        return True

    @classmethod
    def validacao_produto_preco(cls, preco: float) -> bool:
        if not isinstance(preco, (int, float)) or preco <= 0:
            return False
        return True

    @classmethod
    def validacao_produto_quantidade(cls, quantidade: int) -> bool:
        if not isinstance(quantidade, int) or quantidade < 0:
            return False
        return True
