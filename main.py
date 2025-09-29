from mcp.server.fastmcp import FastMCP
from patterns.creational.singleton import PlayerDataManager

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


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


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