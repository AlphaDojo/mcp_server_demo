from abc import ABC, abstractmethod

class LegacyScoreboard(ABC):

    def __init__(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score
        pass

    @abstractmethod
    def display_score(home_score, away_score):
        return print (home_score + " - " + away_score)