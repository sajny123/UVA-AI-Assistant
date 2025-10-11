from mcp.server.fastmcp import FastMCP
from pathlib import Path
import json

mcp = FastMCP("Courses")

DATA_FILE = Path(__file__).parent / "cs_requirements.json"

def load_data() -> dict:
    """Load CS degree requirements"""
    with open(DATA_FILE, 'r') as f: 
        return json.load(f)

@mcp.tool()    
def get_all_requirements() -> str:
    """Gets all requirements"""
    data = load_data()
    return json.dumps(data, indent=2)

@mcp.tool()
def engineering_requirements() -> str:
    """Gets engineering general requirements"""
    data = load_data()

    courses = data["general_requirements"]["courses"]
    return json.dumps(courses, indent=2)

@mcp.tool()
def introduction_programming() -> str:
    """Gets introductory CS requirements"""
    data = load_data()

    courses = data["introduction_to_programming"]["courses"]
    return json.dumps(courses, indent=2)

@mcp.tool()
def foundations() -> str:
    """Gets foundation CS requirements"""
    data = load_data()

    courses = data["foundation_courses"]["courses"]
    return json.dumps(courses, indent=2)

@mcp.tool()
def upper_level() -> str:
    """Gets upper-level CS requirements"""
    data = load_data()

    courses = [data["upper_level_required"]["software_engineering"]] + data["upper_level_required"]["senior_thesis"]["courses"]
    return json.dumps(courses, indent=2)

@mcp.tool()
def apma_electives() -> str:
    """Gets applied mathematics requirements"""
    data = load_data()

    courses = [data["apma_electives"]["required"]] + data["apma_electives"]["courses"]
    return json.dumps(courses, indent=2)

def main():
    print("MCP server is running")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()

