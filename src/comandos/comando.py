from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def execute(self):
        pass
