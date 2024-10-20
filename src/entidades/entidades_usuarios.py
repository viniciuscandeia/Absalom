from uuid import uuid4


class Usuario:
    def __init__(self, id_ = None, nome = "", username = "", email = "", senha = "", tipo = "", id_loja = -1):
        self.id_: int = id_ if id_ else uuid4().hex
        self.nome: str = nome
        self.username: str = username
        self.email: str = email
        self.senha: str = senha
        self.tipo: str = tipo
        self.id_loja: int = id_loja

    def __str__(self) -> str:
        return f"[{self.id_}] Nome: {self.nome}, Email: {self.email}"
