# SSE (Server-Sent Events) Transport for MCP Base

This document explains the SSE (Server-Sent Events) transport layer for MCP Base. SSE enables the server to push real-time updates to clients over HTTP, making it ideal for web-based integrations, dashboards, and agentic workflows that require streaming responses.

---

## 🚦 What is SSE Transport?

SSE is a web technology that allows a server to send updates to clients over a single, long-lived HTTP connection. In the context of MCP, SSE enables the server to stream tool results, logs, or events to clients in real time.

---

## 🛠️ How to Use

### 1. Start the Server with SSE

```bash
python main.py --transport=sse
```

### 2. Client Integration

- Web clients or agent frameworks can connect to the server’s SSE endpoint (e.g., `http://localhost:PORT/sse`).
- Example client code (JavaScript):
  ```js
  const eventSource = new EventSource('http://localhost:PORT/sse');
  eventSource.onmessage = (event) => {
    console.log('Received:', event.data);
  };
  ```

---

## ⚙️ Configuration

- The transport can be selected via CLI argument (`--transport=sse`) or environment variable (`MCP_TRANSPORT=sse`).
- Port and host are configurable via `.env` or CLI (e.g., `PORT=8080`).
- CORS and authentication can be enabled for security.

---

## 🔒 Security Considerations

- SSE endpoints should be protected if exposed to public networks.
- Use HTTPS in production to secure data in transit.
- Implement authentication and authorization as needed.

---

## 🧩 Extending SSE Transport

- The SSE transport implementation is modular and can be extended for custom event types, authentication, or protocol enhancements.
- See `/src/transports/sse/` for the implementation and extension points.

---

## 📝 Best Practices

- Use SSE for web dashboards, real-time monitoring, or any use case requiring streaming updates.
- For local or CLI-based integration, prefer STDIO transport.
- For RESTful APIs, consider HTTP transport.

---

## 📚 Further Reading

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/introduction)
- [MCP Base README](../../../README.md)
- [Other Transport Layers](../)

---

SSE is a powerful option for real-time, web-based MCP integrations in Python. For questions or issues, see the main project README or open an issue.
