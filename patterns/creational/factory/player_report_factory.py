from abc import ABC, abstractmethod
from .player_report import PlayerReport
from typing import Dict

class SummaryReport(PlayerReport):
    def generate(self):
        return f"{self.player_name}: Summary report"

class DetailedReport(PlayerReport):
    def generate(self):
        return f"{self.player_name}: Detailed report with stats and history"

class StatsOnlyReport(PlayerReport):
    def generate(self):
        return f"{self.player_name}: Stats-only report"

class ReportFactory(ABC):
    @abstractmethod
    def generate_report(self, player_name: str) -> PlayerReport:
        pass

class SummaryFactory(ReportFactory):

    def generate_report(self, player_name) -> PlayerReport:
        return SummaryReport(player_name)
    
class DetailedFactory(ReportFactory):

    def generate_report(self, player_name) -> PlayerReport:
        return DetailedReport(player_name)
    
class StatsOnlyFactory(ReportFactory):

    def generate_report(self, player_name) -> PlayerReport:
        return StatsOnlyReport(player_name)

class DynamicReportFactory:
    def generate_report(self, player_name: str, report_type: str) -> PlayerReport:  

        reports: Dict[str, ReportFactory] = {
            "summary": SummaryFactory(),
            "detailed": DetailedFactory(),
            "stats-only": StatsOnlyFactory()
        }

        if report_type not in reports:
            raise ValueError(f"Unknown report type: {report_type}")
            
        return reports[report_type].generate_report(player_name)    