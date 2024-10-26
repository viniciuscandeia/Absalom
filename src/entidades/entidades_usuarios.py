from .entidade import Entidade


class Usuario(Entidade):
    def __init__(
        self,
        id_: int,
        nome: str,
        username: str,
        email: str,
        senha: str,
        tipo: str,
        id_loja: int,
    ):
        super().__init__(id_)
        self.nome: str = nome
        self.username: str = username
        self.senha: str = senha
        self.tipo: str = tipo
        self.id_loja: int = id_loja

    def __str__(self) -> str:
        return f"[{self.id_}] Nome: {self.nome}, Email: {self.email}"
