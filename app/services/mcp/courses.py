from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from pathlib import Path
import json

mcp = FastMCP("Courses")

DATA_FILE = Path(__file__).parent / "cs_requirements.json"

def load_data():
    """Load CS degree requirements"""
    with open(DATA_FILE, 'r') as f: 
        return json.load(f)
    
def get_all_requirements():
    data = load_data()
    return json.dumps(data, indent=2)

def engineering_requirements():
    data = load_data()

    courses = data["general_requirements"]["courses"]
    return json.dumps(courses, indent=2)

def introduction_programming():
    data = load_data()

    courses = data["introduction_to_programming"]["courses"]
    return json.dumps(courses, indent=2)

def foundations():
    data = load_data()

    courses = data["foundation_courses"]["courses"]
    return json.dumps(courses, indent=2)

def upper_level():
    data = load_data()

    courses = [data["upper_level_required"]["software_engineering"]] + data["upper_level_required"]["senior_thesis"]["courses"]
    return json.dumps(courses, indent=2)

def apma_electives():
    data = load_data()

    courses = [data["apma_electives"]["required"]] + data["apma_electives"]["courses"]
    return json.dumps(courses, indent=2)

