"""
app/tools/__init__.py

This file is for registering tool classes from app/tools/ with the MCP server.

How to use:
- Import your tool classes here.
- Register each tool using the @mcp.tool() decorator inside the register_tools function.
- See the example template below for guidance.

To add a new tool class:
1. Create your tool class in app/tools/ (e.g., my_tool.py).
2. Import your tool class here.
3. Register it in the register_tools function.

For simple tools, you can also define and register them directly in app/tools.py.
"""

def register_tools(mcp):
    # Example tool class registration (uncomment and customize)
    #
    # from app.tools.my_tool import MyTool
    # @mcp.tool()
    # async def my_tool_entrypoint(...):
    #     tool = MyTool(...)
    #     result = await tool()
    #     return result
    #
    # Add more tool registrations below as needed.
    pass  # Remove this line when you add your first tool
