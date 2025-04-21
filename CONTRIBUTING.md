# Contributing to MCP Base

Thank you for your interest in contributing! MCP Base is a solid, foundational starting point for building Model Context Protocol (MCP) servers in **Python**. We welcome contributions of all kinds—code, documentation, tests, and ideas.

---

## 🚦 How to Contribute

1. **Fork the repository** and create your branch from `main`.
2. **Write clear, modular Python code** following the project’s structure and style.
3. **Add or update tests** in `/tests/` for any new features or bug fixes.
4. **Document your changes** in the relevant README or code comments.
5. **Submit a pull request** with a clear description of your changes and why they are needed.

## First-Time Contributors

For first time contributors, follow the instructions below:

## Step 1: Set Up Your Environment

Follow these steps to get the project running locally:

1. Fork the repo by clicking the "Fork" button in the top right corner.
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mcp-base.git
   cd mcp-base
Install dependencies:

bash
pip install -r requirements.txt
Run the tests to ensure everything works.

##Step 2: Find an Issue
Look for "good first issue" labels

Comment to claim the issue

Ask questions if anything is unclear

Step 3: Create Your Branch
Branch off from main using a descriptive name:

bash
git checkout -b fix/issue-101-doc-typo

##Step 4: Make Your Change
Write clean, modular code that follows the style guide:

Use PEP8 and type hints

Run Black to format your code

Add/modify tests if needed (in /tests/)

Comment on anything that's not obvious

If you're adding a tool, prompt, or transport, document it!

##Step 5: Commit and Push
bash
git add .
git commit -m "Fix typo in X doc"
git push origin fix/issue-101-doc-typo

##Step 6: Open a Pull Request
Go to your fork on GitHub and click "Compare & pull request."

Fill in:

A clear title and description

Mention the issue it closes (e.g., Closes #101)

What you did and why

##Step 7: What Happens Next?
After you submit your PR:

A maintainer will review it and may suggest changes

You can update your PR by pushing new commits

Once approved, it will be merged!

Congrats, you're now an MCP Base contributor! 🎉
 

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
