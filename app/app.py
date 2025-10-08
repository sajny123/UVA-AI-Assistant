from flask import Flask
from app.routes import setup_routes
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    
    setup_routes(app)

    return app
