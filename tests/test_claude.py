import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.claude_client import get_claude_response

def test_claude():
    print("Testing Claude Client")
    response = get_claude_response("Hello! Explain the history of UVA in two sentences.")
    print (response)

if __name__ == "__main__":
    test_claude()