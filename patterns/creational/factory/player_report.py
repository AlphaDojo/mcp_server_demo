from abc import ABC, abstractmethod

class PlayerReport(ABC):

    def __init__(self, player_name):
        self.player_name = player_name

    @abstractmethod
    def generate(self):
        pass