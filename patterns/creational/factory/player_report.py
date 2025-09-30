from abc import ABC, abstractmethod

class PlayerReport(ABC):
    """report interface"""

    def __init__(self, player_name):
        self.player_name = player_name

    @abstractmethod
    def generate(self):
        """generates a report"""
        pass