from src.memento.caretaker import Caretaker


class CaretakerLoja(Caretaker):
    def __init__(self):
        super().__init__()

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]

    def get_mementos(self):
        for memento in self.mementos:
            print(memento.get_state())
