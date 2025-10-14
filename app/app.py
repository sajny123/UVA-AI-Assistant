from flask import Flask, send_from_directory
from app.routes import setup_routes
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__, static_folder='../frontend/project/dist', static_url_path='/')
    app.config["JSON_SORT_KEYS"] = False
    
    setup_routes(app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        return send_from_directory(app.static_folder, 'index.html')

    return app
