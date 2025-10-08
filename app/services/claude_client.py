import os, json, requests
from dotenv import load_dotenv

load_dotenv()

def get_claude_response(prompt):
    API_KEY = os.getenv("ANTHROPIC_API_KEY")
    url = "https://api.anthropic.com/v1/messages"
    model = "claude-sonnet-4-5"
    max_tokens = 1000

    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY, 
        "anthropic_version": "2023-06-01"
    }

    data = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    response = requests.post(url=url, headers=headers, json=data)
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
        print (F"Unexpected reponse structure: {e}")
        print (json.dumps(response.json(), indent=2))
        return
    