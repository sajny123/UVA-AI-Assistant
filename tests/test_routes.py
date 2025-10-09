import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.app import create_app

def test_home():
    app = create_app()
    client = app.test_client()

    print ("Testing home")
    response = client.get('/')
    if response.status_code == 200:
        print ("Home is working")
    else:
        print (response.status_code)

def test_health():
    app = create_app()
    client = app.test_client()

    print ("Testing health")
    response = client.get('/health')
    if response.status_code == 200:
        print ("Health is normal")
    else:
        print (response.status_code)

BASE_URL = "http://localhost:3000"

def test_ask():
    app = create_app()
    client = app.test_client()

    print ("Testing Ask Endpoint")
    data = {
        "question": "How old is UVA"
    }
    response = client.post(BASE_URL + "/ask", json=data)
    if response.status_code == 200:
        print (response)
    else: 
        print (response.status_code)

if __name__ == "__main__":
    # test_home()
    # test_health()
    test_ask()