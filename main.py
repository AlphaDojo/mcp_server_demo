from mcp.server.fastmcp import FastMCP
from .patterns.creational.singleton.player_data import PlayerDataManager
from .patterns.creational.factory.player_report_factory import DynamicReportFactory

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

# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."