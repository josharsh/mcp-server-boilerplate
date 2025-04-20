# STDIO Transport for MCP Base

This document explains the STDIO transport layer for MCP Base. STDIO is the default and most universal transport for MCP servers, enabling communication via standard input/output streams. It is ideal for CLI integration, agentic workflows, and environments where network access is restricted.

---

## 🚦 What is STDIO Transport?

STDIO transport allows the MCP server to communicate with clients (such as LLMs, agent frameworks, or CLI tools) using standard input and output streams. This is the most direct and secure way to connect an MCP server to a local or containerized client.

---

## 🛠️ How to Use

### 1. Start the Server with STDIO

```bash
python main.py --transport=stdio
```

### 2. Client Integration

- MCP clients (e.g., Claude Desktop, Cline, custom agents) can launch the server as a subprocess and communicate via STDIO.
- Example client configuration:
  ```json
  {
    "mcpServers": {
      "my-server": {
        "command": "python",
        "args": ["main.py", "--transport=stdio"]
      }
    }
  }
  ```

---

## ⚙️ Configuration

- The transport can be selected via CLI argument (`--transport=stdio`) or environment variable (`MCP_TRANSPORT=stdio`).
- Allowed directories, environment variables, and other options are configured in `.env` or via CLI.

---

## 🔒 Security Considerations

- STDIO transport is local-only by default; no network exposure.
- Ensure the server is launched in a secure environment, especially if handling sensitive files or data.
- All file operations are sandboxed to allowed directories.

---

## 🧩 Extending STDIO Transport

- The STDIO transport implementation is modular and can be extended for custom logging, input/output formatting, or protocol enhancements.
- See `/src/transports/stdio/` for the implementation and extension points.

---

## 📝 Best Practices

- Use STDIO for local development, testing, and secure agent integration.
- For remote or web-based clients, consider using SSE or HTTP transports (see their respective docs).

---

## 📚 Further Reading

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/introduction)
- [MCP Base README](../../../README.md)
- [Other Transport Layers](../)

---

STDIO is the recommended starting point for most Python MCP server projects. For questions or issues, see the main project README or open an issue.
