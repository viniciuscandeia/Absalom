from src.memento.memento import Memento


class  Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento:Memento) -> Memento:
        self.mementos.append(memento)
        return memento

    def get_memento(self, index:int) -> Memento:
        return self.mementos[index]