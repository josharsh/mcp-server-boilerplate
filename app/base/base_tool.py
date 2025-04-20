import logging
from app.base.api_client import APIClient

class BaseTool:
    """
    Abstract base class for all MCP tools.
    Provides access to the shared API client and logger.
    """
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
        self.logger = logging.getLogger(self.__class__.__name__)

    # Optionally, add shared error handling, validation, or result formatting here
