import logging

class BasePrompt:
    """
    Abstract base class for all MCP prompts.
    Provides a logger and a place for shared prompt utilities.
    """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    # Optionally, add shared formatting, context helpers, or validation here
