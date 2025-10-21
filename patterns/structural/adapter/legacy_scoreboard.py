from abc import ABC, abstractmethod

class LegacyScoreboard(ABC):

    def __init__(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score
        

    def display_score(self, home_score, away_score):
        return f"{self.home_score} - {self.away_score}"