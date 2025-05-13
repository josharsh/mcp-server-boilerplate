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

from app.tools.helloworld import HelloTool
from app.tools.simplecalc import SimpleCalc
from app.base.api_client import APIClient
import logging

logger = logging.getLogger("app.tools")

def register_tools(mcp):
    logger.info("Registering tools...")

    api_client = APIClient()

    @mcp.tool()
    async def hello_tool(name: str):
        """
        Returns a greeting for the given name.
        Args:
            name: The name to greet.
        Returns:
            A greeting string.
        """
        tool = HelloTool(api_client)
        return await tool.run(name)

    @mcp.tool()
    async def simple_calculator(num1: float = 0, operator: str = "add", num2: float = 0):
        """
        Simple calculator tool.
        Args:
            num1: first number
            operator: operation (add, subtract, multiply, divide)
            num2: second number
        Returns:
            A result dictionary with the result of the operation.
        """
        tool = SimpleCalc(api_client)
        return await tool.run(num1, operator, num2)
