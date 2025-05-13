from app.base.base_prompt import BasePrompt

class WelcomePrompt(BasePrompt):
    def __call__(self) -> str:
        return "Welcome to the MCP server! How can I assist you today?"