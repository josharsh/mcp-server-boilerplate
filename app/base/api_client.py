import httpx
import logging
from typing import Any, Dict, Optional
from app.config import settings

class APIClient:
    """
    Centralized async API client for all tools.
    Handles GET/POST requests, error handling, and logging.
    """
    def __init__(self):
        self.base_url = settings.api_base_url.rstrip("/")
        self.api_key = settings.api_key
        self.deployment = settings.deployment
        self.api_version = settings.api_version
        self.logger = logging.getLogger("APIClient")

    def _build_headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }
        if extra_headers:
            headers.update(extra_headers)
        return headers

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Any:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"GET {url} params={params}")
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=self._build_headers(headers))
            response.raise_for_status()
            return response.json()

    async def post(self, endpoint: str, data: Any = None, headers: Optional[Dict[str, str]] = None) -> Any:
        url = f"{self.base_url}/openai/deployments/{self.deployment}/{endpoint.lstrip('/')}?api-version={self.api_version}"
        self.logger.info(f"POST {url} data={data}")
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=self._build_headers(headers))
            response.raise_for_status()
            return response.json()
