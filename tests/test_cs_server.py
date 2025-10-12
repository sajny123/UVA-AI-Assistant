import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.claude_client import MCP

def test_cs():
    print("Testing Claude Client CS MCP Server")
    response = MCP.ask_claude("What CS courses do I have to take for a CS degree through the school of Engineering?")
    print (response)

if __name__ == "__main__":
    test_cs()