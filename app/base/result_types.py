from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class ToolResult:
    success: bool
    data: Any = None
    error: Optional[str] = None

@dataclass
class PromptResult:
    content: str
    metadata: Optional[dict] = None
