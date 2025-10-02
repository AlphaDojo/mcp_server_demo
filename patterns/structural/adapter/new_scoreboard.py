from .legacy_scoreboard import LegacyScoreboard
from .score_processor import ScoreProcessor


class ScoreboardAdapter(ScoreProcessor):

    def __init__(self, legacy_scoreboard: LegacyScoreboard):
        self.legacy_scoreboard = legacy_scoreboard

    def display_score(self, home: str, away: str, home_runs: int, away_runs: int, inning: int):
        return {
            "home_team": home,
            "home_runs": home_runs,
            "away_team": away,
            "away_runs": away_runs,
            "innings": inning
        }