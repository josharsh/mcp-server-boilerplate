import httpx
import logging
from typing import Any, Dict, Optional

class APIClient:
    """
    Centralized async API client for all tools.
    Handles GET/POST requests, error handling, and logging.
    """
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.logger = logging.getLogger("APIClient")

    def _build_headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json"
        }
        if self.api_key:
            headers["X-API-Key"] = self.api_key
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
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"POST {url} data={data}")
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=self._build_headers(headers))
            response.raise_for_status()
            return response.json()
