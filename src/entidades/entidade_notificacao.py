from src.entidades.entidade import Entidade


class Notificacao(Entidade):
    def __init__(self, id_: int, mensagem: str, from_user_id: int, to_loja_id: int):
        super().__init__(id_)
        self.id_ = id_
        self.mensagem = mensagem
        self.from_user_id = from_user_id
        self.to_loja_id = to_loja_id

    def __str__(self) -> str:
        return f"[{self.id_}] [from user(id): {self.from_user_id}] [to loja(id): {self.to_loja_id}] -> {self.mensagem}"
