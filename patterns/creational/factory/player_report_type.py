from .player_report import PlayerReport

class SummaryReport(PlayerReport):
    def generate(self):
        return f"{self.player_name}: Summary report"

class DetailedReport(PlayerReport):
    def generate(self):
        return f"{self.player_name}: Detailed report with stats and history"

class StatsOnlyReport(PlayerReport):
    def generate(self):
        return f"{self.player_name}: Stats-only report"
