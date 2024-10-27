from src.entidades.entidade_loja import Loja
from src.memento.memento import Memento


class MementoLoja(Memento):
    def __init__(self, state: Loja):
        super().__init__(state)

    def get_state(self):
        return self.state
