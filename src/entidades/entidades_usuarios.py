
class Usuario:

    def __init__(self, id_: int, nome: str, username: str, email: str, senha: str, tipo: str, id_loja: int):
        self.id_: int = id_
        self.nome: str = nome
        self.username: str = username
        self.email: str = email
        self.senha: str = senha
        self.tipo: str = tipo
        self.id_loja: int = id_loja

    def __str__(self) -> str:
        return f"[{self.id_}] Nome: {self.nome}, Email: {self.email}"
