from abc import ABC, abstractmethod


class Originator(ABC):
    def __init__(self, state):
        self.state = state

    @abstractmethod
    def create_memento(self):
        pass

    @abstractmethod
    def restore(self, memento):
        pass

    @abstractmethod
    def set_state(self, state):
        pass

    @abstractmethod
    def get_state(self):
        pass