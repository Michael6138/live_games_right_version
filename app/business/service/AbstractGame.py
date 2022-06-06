from abc import ABC, abstractmethod


class AbstractGame(ABC):
    @abstractmethod
    def play(self, difficulty):
        pass
