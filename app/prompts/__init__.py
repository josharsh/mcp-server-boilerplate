"""
app/prompts/__init__.py

This file is for registering prompt classes from app/prompts/ with the MCP server.

How to use:
- Import your prompt classes here.
- Register each prompt using the @mcp.prompt() decorator inside the register_prompts function.
- See the example template below for guidance.

To add a new prompt class:
1. Create your prompt class in app/prompts/ (e.g., my_prompt.py).
2. Import your prompt class here.
3. Register it in the register_prompts function.

For simple prompts, you can also define and register them directly in app/prompts.py.
"""
from app.prompts.welcome import WelcomePrompt

def register_prompts(mcp):
    print("Registering prompts...")

    @mcp.prompt()
    def welcome_prompt() -> str:
        """
        Example Welcome Prompt.
        """
        prompt = WelcomePrompt()
        result = prompt()
        return result

    @mcp.prompt()
    def example_prompt() -> str:
        """
        Example prompt description or template.
        You can use triple-quoted strings for multi-line prompts.
        """
        return example_prompt.__doc__
