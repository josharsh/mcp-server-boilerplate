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

def register_prompts(mcp):
    # Example prompt class registration (uncomment and customize)
    #
    # from app.prompts.my_prompt import MyPrompt
    # @mcp.prompt()
    # def my_prompt_entrypoint() -> str:
    #     prompt = MyPrompt()
    #     result = prompt()
    #     return result
    #
    # Add more prompt registrations below as needed.
    pass  # Remove this line when you add your first prompt
