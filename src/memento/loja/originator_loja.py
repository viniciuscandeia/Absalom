from copy import deepcopy

from src.entidades.entidade_loja import Loja
from src.memento.loja.memento_loja import MementoLoja
from src.memento.originator import Originator


class OriginatorLoja(Originator):
    def __init__(self, state: Loja = None):
        super().__init__(state)

    def create_memento(self):
        return MementoLoja(deepcopy(self.state))

    def restore(self, memento):
        self.state = memento.get_state()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


