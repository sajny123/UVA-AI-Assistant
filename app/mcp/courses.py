from mcp.server.fastmcp import FastMCP
from pathlib import Path
import json, os

mcp = FastMCP("Courses")

def load_data() -> dict:
    """Load CS degree requirements"""
    try: 
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        file_path = os.path.join(project_root, 'data', 'cs_requirements.json')
        with open(file_path, 'r') as f: 
            return json.load(f)
    except FileNotFoundError:
        return {"error": "File could not be found"}
    except Exception as e:
        return {"error": f"An unexpected error occured: {e}"}

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

