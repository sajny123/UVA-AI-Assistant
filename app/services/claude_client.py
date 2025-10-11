import os, json, requests
from dotenv import load_dotenv
from mcp.client import MCPClient

load_dotenv()

def connect_mcp():
    client = MCPClient()
    client.connect("Courses")
    return client


def get_claude_response(prompt):
    API_KEY = os.getenv("ANTHROPIC_API_KEY")
    url = "https://api.anthropic.com/v1/messages"
    model = "claude-sonnet-4-5"
    max_tokens = 1000

    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY, 
        "anthropic-version": "2023-06-01"
    }

    client = connect_mcp()
    tools = client.list_tools()
    tool_definitions = [
        {
            "name": tool["name"],
            "description": tool["description"]
        }
        for tool in tools
    ]

    initial_data = {
        "model": model,
        "max_tokens": max_tokens,
        "tools": tool_definitions,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=initial_data)

    content = response.json().get("content", [{}])
    if content and "tool_calls" in content[0]:
        tool_call = content[0]["tool_calls"][0]
        tool_name = tool_call["name"]
        args = tool_call.get("arguments", {})

        print(f"Claude requested {tool_name}")

        result = client.call_tool(tool_name, **args)

        new_data = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                },
                {
                    "role": "tool",
                    "content": json.dumps(result)    
                }
            ]
        }
        response = requests.post(url, headers=headers, json=new_data)        

    try: 
        if response.status_code == 200: 
            print(response.json()['content'][0]['text'])
            return (response.json()['content'][0]['text'])
        else:
            error_type = response.json()['error']['type']
            error_message = response.json()['error']['message']
            print (f"Error type: {error_type}")
            print (f"Error message: {error_message}")
            return
    except requests.exceptions.RequestException as e:
        print (f"Request failed: {e}")
        return
    except KeyError as e:
        print (f"Unexpected response structure: {e}")
        print (json.dumps(response.json(), indent=2))
        return
    