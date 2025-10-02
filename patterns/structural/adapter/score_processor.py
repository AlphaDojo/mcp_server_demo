from abc import ABC, abstractmethod


class ScoreProcessor(ABC):
    
    @abstractmethod
    def display_score(self, home: str, away: str, home_runs: int, away_runs: int, inning: int) ->  dict:
        pass