# 🧠 Claude Desktop + MCP Tools

This repo demonstrates how to use the **Model Context Protocol (MCP)** to connect Claude Desktop with your own tools and data sources.

It includes:
- `main.py`: A basic MCP tool (e.g., add numbers, greet a user)
- `sticky_note.py`: A mini sticky note system that lets Claude create, update, and fetch notes
- All configured to run immediately after cloning the repo

---

## 📦 Features

| File            | Description                                      |
|-----------------|--------------------------------------------------|
| `main.py`       | Registers a basic MCP server with simple tools   |
| `sticky_note.py`| Advanced MCP server with note-taking tools       |
| `notes.json`    | Storage file for sticky notes                    |

---

## 🛠 Requirements

- Python 3.8+
- [Claude Desktop](https://www.anthropic.com/)
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) (a modern Python package manager)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Anup-repo/own-mcp-server.git
cd own-mcp-server
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```
### 3. Install uv

You can install uv via pip:

```bash
pip install uv
```
## Official docs: https://docs.astral.sh/uv/getting-started/installation

### 4. Create and Initialize MCP Project

```bash
uv init .
uv add "mcp[cli]"
```

### 5. Create MCP Server

```bash
uv run mcp install main.py
```

### 6. Run the MCP Server

```bash
You’ll now see Demo as a tool in Claude Desktop. Try:

“Add 3 + 2”
```
### 7. Run Sticky Note Server (sticky_note.py)

```bash
uv run mcp install sticky_note.py
```

## 🧪 Example Use Cases in Claude

1. Create Notes

* Ask Claude:
    Create 10 sticky notes about RCB.


2. Get Specific Note
Get sticky note with ID 3.

3. Explore Resources
Click on ➕ and select get_latest_note.
Then ask: Summarize this note in 5 lines.

4. Summarize All Notes
Click ➕, select notes://example, then run note_summary.

Claude will summarize your sticky notes using the custom prompt.

### 🧱 File Structure
```bash
mcp-server/
│
├── main.py                # Basic add/greeting tool
├── sticky_note.py         # Sticky note toolset
├── notes.json             # Note storage
├── pyproject.toml         # MCP project metadata
└── README.md              # This file
```

### 🛠 Troubleshooting
If the tools don’t show up in Claude Desktop:

Restart Claude Desktop

Go to Settings → Developer → Linked Servers

If not linked:

Click Edit Config

Update the full path to uv:

```json
{
  "uv": "/your/full/path/to/uv"
}
```

You can find the path using:

```bash
which uv       # macOS/Linux
where uv       # Windows
```

Save, close, and reopen Claude Desktop

## Checkout medium article for more details: [How to Build a Local MCP Server](https://medium.com/@yourusername/how-to-build-a-local-mcp-server-1234567890)