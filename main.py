from mcp.server.fastmcp import FastMCP
from .patterns.creational.singleton.player_data import PlayerDataManager
from .patterns.creational.factory.player_report_factory import DynamicReportFactory
from .patterns.structural.adapter.legacy_scoreboard import LegacyScoreboard
from .patterns.structural.adapter.new_scoreboard import ScoreboardAdapter

# Create an MCP server
mcp = FastMCP("Demo")
manager = PlayerDataManager()

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def get_player_stat_tool(player_name: str, stat: str) -> str:
    """Return the specified stat for the given player (e.g., batting_average, home_runs)"""
    return str(manager.get_player_stat(player_name, stat))


@mcp.tool()
def get_player_report(player_name: str, report_type: str) -> str:
    """Return the specified report for the given player (e.g. summary, detailed, stats-only)"""
    factory = DynamicReportFactory()
    report_instance =  factory.generate_report(player_name, report_type)

    return report_instance.generate()

@mcp.tool()
def get_scoreboard(home: str, away: str, home_runs: int, away_runs: int, innings: int) -> str:
    legacy = LegacyScoreboard()
    adapter = ScoreboardAdapter(legacy)

    return adapter.display_score(home, away, home_runs, away_runs, innings)