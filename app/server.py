from mcp.server.fastmcp import FastMCP
from app.config import settings
from app.tools import register_tools
from app.prompts import register_prompts

# Create server with a descriptive name
print("Starting MCP server...")
print(f"Settings: {settings.dict()}")

mcp = FastMCP("MCP Base Server")

# Register all tools and prompts (now from modular registries)
register_tools(mcp)
register_prompts(mcp)

print("Server is ready to accept requests.")
