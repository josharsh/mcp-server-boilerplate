# MCP Base

A solid, foundational starting point for MCP projects. MCP Base is a production-ready, extensible template for building Model Context Protocol (MCP) servers in **Python**. Rapidly create, extend, and deploy MCP servers that expose tools, prompts, and resources to LLMs and agentic clients.

---

## 🚀 What is This?

This is a **Python starter base**—not a specific server implementation. It provides a modular, well-documented foundation for building your own MCP servers in Python, supporting multiple transport layers (STDIO, SSE, HTTP, etc.), and demonstrating best practices for security, extensibility, and maintainability.

---

## 🏗️ Architecture Overview

```
.
├── src/
│   ├── base/                # Base classes for tools, prompts, resources
│   ├── tools/               # Example tools (filesystem, API, prompt, etc.)
│   ├── resources/           # Example resources (static/dynamic)
│   ├── prompts/             # Example prompts (text generation, summarization)
│   ├── transports/          # Transport layer implementations & docs
│   │   ├── stdio/
│   │   │   └── README.md
│   │   ├── sse/
│   │   │   └── README.md
│   │   └── ...
│   ├── config.py            # Configuration and environment management
│   ├── server.py            # Server instantiation and registration
│   └── main.py              # Entrypoint: selects transport, starts server
├── tests/                   # Example tests for tools/resources
├── Dockerfile               # Containerized deployment
├── requirements.txt / pyproject.toml
├── README.md                # This file
├── CONTRIBUTING.md
└── ...
```

---

## Architecture Diagram

```mermaid
flowchart TD
    %% Client
    Client["Client (LLM/Agent)"]:::external

    %% Transports Layer
    subgraph "Transport Layer"
        direction TB
        STDIO["STDIO Transport"]:::plugin
        SSE["SSE Transport"]:::plugin
        HTTP["HTTP Transport"]:::plugin
    end

    %% Entrypoint
    Main["main.py (Entrypoint)"]:::core

    %% Configuration
    Config["Config & Env (app/config.py)"]:::core

    %% Server Core
    subgraph "MCP Server Core"
        direction TB
        Dispatcher["Transport Dispatcher"]:::core
        ToolReg["Tool Registry"]:::core
        PromptReg["Prompt Registry"]:::core
        ResourceReg["Resource Registry"]:::core
    end

    %% Base Modules
    subgraph "Base Modules (app/base)"
        direction TB
        BaseTool["BaseTool"]:::core
        BasePrompt["BasePrompt"]:::core
        APIClient["APIClient"]:::core
        ResultTypes["ResultTypes"]:::core
    end

    %% Plugin System - Tools
    subgraph "Plugins - Tools"
        direction TB
        ToolsLoader["Tools Loader"]:::plugin
        GlobalContext["global_context"]:::plugin
        ListUploads["list_uploads"]:::plugin
    end

    %% Plugin System - Prompts
    subgraph "Plugins - Prompts"
        direction TB
        PromptsLoader["Prompts Loader"]:::plugin
        ActionItems["action_items"]:::plugin
        ProjectInsights["project_insights"]:::plugin
        Welcome["welcome"]:::plugin
    end

    %% External Integrations
    subgraph "External Integrations"
        direction TB
        APISvc["External APIs"]:::external
        FileSys["Filesystem (Sandbox)"]:::external
        EnvVars["Environment Variables"]:::external
    end

    %% Deployment
    subgraph "Deployment Infrastructure"
        direction TB
        Dockerfile["Dockerfile"]:::deploy
        DockerCompose["docker-compose.yml"]:::deploy
        DevSetup["dev-setup.sh"]:::deploy
        DockerRun["docker-run.sh"]:::deploy
    end

    %% Docs for Transports
    subgraph "Transport Documentation"
        direction TB
        DocStdio["docs/transports/stdio/README.md"]:::external
        DocSSE["docs/transports/sse/README.md"]:::external
    end

    %% Connections
    Client -->|sends request| STDIO
    Client -->|sends request| SSE
    Client -->|sends request| HTTP

    STDIO --> Main
    SSE --> Main
    HTTP --> Main

    Main -->|loads| Config
    Main -->|initializes| Dispatcher

    Dispatcher -->|routes| ToolReg
    Dispatcher -->|routes| PromptReg
    Dispatcher -->|routes| ResourceReg

    ToolReg --> ToolsLoader
    PromptsLoader --> PromptReg
    ToolsLoader --> GlobalContext
    ToolsLoader --> ListUploads
    PromptsLoader --> ActionItems
    PromptsLoader --> ProjectInsights
    PromptsLoader --> Welcome

    GlobalContext -->|uses| APIClient
    ListUploads -->|uses| FileSys
    ActionItems -->|uses| BaseTool
    ProjectInsights -->|uses| BasePrompt
    Welcome -->|uses| ResultTypes

    BaseTool --> ToolReg
    BasePrompt --> PromptReg
    APIClient --> APISvc
    ResultTypes -->|returned| Dispatcher

    Config -->|env| EnvVars

    Dispatcher -->|responds| Client

    Dockerfile -->|builds image| Main
    DockerCompose -->|orchestrates| Dockerfile
    DevSetup -->|sets up| EnvVars
    DockerRun -->|runs| DockerCompose

    STDIO --> DocStdio
    SSE --> DocSSE

    %% Click Events
    click Main "https://github.com/josharsh/mcp-server-boilerplate/blob/main/main.py"
    click Config "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/config.py"
    click Dispatcher "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/server.py"
    click BaseTool "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/base/base_tool.py"
    click BasePrompt "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/base/base_prompt.py"
    click APIClient "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/base/api_client.py"
    click ResultTypes "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/base/result_types.py"
    click ToolsLoader "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/tools.py"
    click GlobalContext "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/tools/global_context.py"
    click ListUploads "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/tools/list_uploads.py"
    click PromptsLoader "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/prompts.py"
    click ActionItems "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/prompts/action_items.py"
    click ProjectInsights "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/prompts/project_insights.py"
    click Welcome "https://github.com/josharsh/mcp-server-boilerplate/blob/main/app/prompts/welcome.py"
    click Dockerfile "https://github.com/josharsh/mcp-server-boilerplate/tree/main/Dockerfile"
    click DockerCompose "https://github.com/josharsh/mcp-server-boilerplate/blob/main/docker-compose.yml"
    click DevSetup "https://github.com/josharsh/mcp-server-boilerplate/blob/main/dev-setup.sh"
    click DockerRun "https://github.com/josharsh/mcp-server-boilerplate/blob/main/docker-run.sh"
    click DocStdio "https://github.com/josharsh/mcp-server-boilerplate/blob/main/docs/transports/stdio/README.md"
    click DocSSE "https://github.com/josharsh/mcp-server-boilerplate/blob/main/docs/transports/sse/README.md"

    %% Styles
    classDef core fill:#cce5ff,stroke:#004085,color:#004085
    classDef plugin fill:#d4edda,stroke:#155724,color:#155724
    classDef external fill:#fff3cd,stroke:#856404,color:#856404
    classDef deploy fill:#e2e3e5,stroke:#6c757d,color:#6c757d
```

---

## ✨ Features

- **Multi-Transport Support:** STDIO, SSE, HTTP, and more (see `/src/transports/`)
- **Modular Tools/Prompts/Resources:** Add new features by creating a class and registering it
- **Type-Safe Input Validation:** Uses Pydantic for schemas
- **Security Best Practices:** Directory sandboxing, input validation, error handling
- **Extensible & Maintainable:** Clean separation of concerns, base classes, and registries
- **Production-Ready:** Logging, environment management, Docker support
- **Comprehensive Documentation:** For users and contributors

---

## 🛠️ Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in required values.

### 3. Run the Server

**STDIO Transport:**
```bash
python main.py --transport=stdio
```

**SSE/HTTP Transport:**
See `/src/transports/sse/README.md` and `/src/transports/http/README.md` for details.

---

## 🧩 Adding Tools, Prompts, and Resources

### Tools

- Create a new class in `/src/tools/` inheriting from `BaseTool`
- Implement the required methods and input schema
- Register the tool in the tool registry

### Prompts

- Create a new class in `/src/prompts/` inheriting from `BasePrompt`
- Implement the required methods and input schema
- Register the prompt in the prompt registry

### Resources

- Add static or dynamic resources in `/src/resources/`
- Register them in the resource registry

---

## 🔌 Supported Transports

- **STDIO:** For CLI and agentic integration (see `/src/transports/stdio/README.md`)
- **SSE:** For server-sent events and web clients (see `/src/transports/sse/README.md`)
- **HTTP:** For RESTful or web-based integration (see `/src/transports/http/README.md`)

Each transport is modular and can be extended or replaced.

---

## 🛡️ Security & Best Practices

- All file and directory operations are sandboxed to allowed paths
- Input validation is enforced for all tool/resource inputs
- Error handling is consistent and user-friendly
- Sensitive configuration is managed via environment variables

---

## 🧪 Testing

- Example tests are provided in `/tests/`
- Use Pytest as the test runner
- See CONTRIBUTING.md for test guidelines

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, code style, and PR process.

---

## 📚 Further Reading

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/introduction)
- [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Reference MCP Servers Gallery](https://github.com/modelcontextprotocol/servers)
- [Transport Layer Docs](/src/transports/)

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 💬 Community & Support

- [Discord](https://discord.gg/jHEGxQu2a5)
- [Reddit](https://www.reddit.com/r/modelcontextprotocol)
- [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions)

---

MCP Base is the recommended starting point for all new Python MCP server projects. Fork, extend, and contribute improvements!
