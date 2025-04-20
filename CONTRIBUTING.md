# Contributing to MCP Base

Thank you for your interest in contributing! MCP Base is a solid, foundational starting point for building Model Context Protocol (MCP) servers in **Python**. We welcome contributions of all kinds—code, documentation, tests, and ideas.

---

## 🚦 How to Contribute

1. **Fork the repository** and create your branch from `main`.
2. **Write clear, modular Python code** following the project’s structure and style.
3. **Add or update tests** in `/tests/` for any new features or bug fixes.
4. **Document your changes** in the relevant README or code comments.
5. **Submit a pull request** with a clear description of your changes and why they are needed.

---

## 🧑‍💻 Code Style

- **Python:** Use type hints, PEP8 style, and async where appropriate.
- **Formatting:** Use [Black](https://black.readthedocs.io/) for code formatting.
- **Naming:** Use descriptive names for files, classes, functions, and variables.
- **Comments:** Write clear, concise comments for complex logic and public APIs.

---

## 🏗️ Project Structure

- **/src/base/**: Base classes for tools, prompts, resources
- **/src/tools/**: Each tool in its own file/class
- **/src/prompts/**: Each prompt in its own file/class
- **/src/resources/**: Static/dynamic resources
- **/src/transports/**: Transport layer implementations and docs
- **/tests/**: Tests for tools, prompts, and resources

---

## 🧪 Testing

- Add or update tests for all new features and bug fixes.
- Use [Pytest](https://docs.pytest.org/) as the test runner.
- Ensure all tests pass before submitting a PR.
- Run tests with:
  ```bash
  pytest
  ```

---

## 🔀 Branching & Pull Requests

- Branch from `main` for all changes.
- Use descriptive branch names (e.g., `feature/add-github-tool`, `fix/stdio-bug`).
- Keep pull requests focused and small; one feature or fix per PR.
- Link related issues in your PR description.

---

## 📝 Documentation

- Update the main README.md if your change affects usage or architecture.
- Add or update transport-specific docs in `/src/transports/<transport>/README.md`.
- Document new tools/prompts/resources in their respective directories.

---

## 🛡️ Security

- Never expose sensitive data or credentials in code or documentation.
- Follow best practices for input validation and sandboxing.

---

## 🤝 Code of Conduct

Please be respectful and inclusive. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

---

## 💬 Getting Help

- Open an issue for bugs, feature requests, or questions.
- Join the [Discord community](https://discord.gg/jHEGxQu2a5) for discussion.

---

Thank you for helping make the Python MCP server ecosystem better!
