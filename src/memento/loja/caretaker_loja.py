from src.memento.caretaker import Caretaker


class CaretakerLoja(Caretaker):
    def __init__(self):
        super().__init__()

    def get_mementos(self):
        for memento in self.mementos:
            print(memento.get_state())
