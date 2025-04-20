import os
import logging
from app.server import mcp

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

def main():
    setup_logging()
    logging.info("Starting MCP server...")
    transport_mode = os.environ.get("MCP_TRANSPORT", "stdio")
    if transport_mode in ("web", "sse"):
        mcp.run(transport="sse")
    else:
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
