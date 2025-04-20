"""
app/prompts.py

This file is the entry point for registering your custom MCP prompts.

How to use:
- Define your prompt functions here or import them from app/prompts/ modules.
- Register each prompt using the @mcp.prompt() decorator.
- See the example template below for guidance.

To add a new prompt:
1. Define a function (sync or async) that returns a string (the prompt text).
2. Decorate it with @mcp.prompt().
3. The returned string will be used as the prompt for the MCP client.

For more advanced prompts, organize them as classes in app/prompts/ and import/register them here.
"""

def register_prompts(mcp):
    # Example prompt template (uncomment and customize)
    #
    # @mcp.prompt()
    # def example_prompt() -> str:
    #     """
    #     Example prompt description or template.
    #     You can use triple-quoted strings for multi-line prompts.
    #     """
    #     return example_prompt.__doc__
    #
    # Add more prompts below as needed.
    pass  # Remove this line when you add your first prompt
