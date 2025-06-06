from mcp.server.fastmcp import FastMCP
import json, os

# Initialize the MCP server with proper configuration
mcp = FastMCP(
    "Sticky Note",
    description="A simple sticky note application",
    version="1.0.0"
)

note_file = os.path.join(os.path.dirname(__file__), "notes.json")

# Handle potential directory creation and other edge cases
try:
    if not os.path.exists(note_file):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(note_file), exist_ok=True)
        with open(note_file, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=2)
except (OSError, json.JSONEncodeError) as e:
    print(f"Error creating file: {e}")


def _load_notes():
    if os.path.exists(note_file):
        with open(note_file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def _save_notes(notes):
    with open(note_file, "w") as f:
        json.dump(notes, f, indent=2)

@mcp.tool()
def create_sticky_note(title: str, content: str) -> str:
    """Create a sticky note"""
    notes = _load_notes()
    note_id = str(len(notes) + 1)
    notes[note_id] = {"title": title, "content": content}
    _save_notes(notes)
    return f"Sticky note created with ID: {note_id}"

@mcp.tool()
def get_sticky_note(id: str) -> str:
    """Get a sticky note"""
    notes = _load_notes()
    if id in notes:
        note = notes[id]
        return f"{note['title']}: {note['content']}"
    return f"No sticky note found with ID: {id}"

@mcp.tool()
def update_sticky_note(id: str, title: str, content: str) -> str:
    """Update a sticky note"""
    notes = _load_notes()
    if id in notes:
        notes[id] = {"title": title, "content": content}
        _save_notes(notes)
        return f"Sticky note updated: {id}"
    return f"No sticky note found with ID: {id}"

@mcp.resource("sticky-note://latest")
def get_latest_sticky_note() -> str:
    """Get the latest sticky note"""
    notes = _load_notes()
    if not notes:
        return "No sticky notes found"
    latest_id = max(notes.keys(), key=int)
    note = notes[latest_id]
    return f"{note['title']}: {note['content']}"

@mcp.prompt()
def note_summary(prompt: str) -> str:
    """Summarize the latest sticky note"""
    notes = _load_notes()
    if not notes:
        return "No sticky notes found"
    latest_id = max(notes.keys(), key=int)
    note = notes[latest_id]
    return f"Summary of the latest sticky note: {note['title']}: {note['content']}"

# Make sure the server is properly initialized
if __name__ == "__main__":
    mcp.run()
    