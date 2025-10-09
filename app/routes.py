from app.services.claude_client import get_claude_response
from flask import request, jsonify

def setup_routes(app):

    @app.route('/')
    def home():
        return jsonify({"message": "API is running"})
    
    @app.route('/health')
    def health():
        return jsonify({"status": "healthy"})

    @app.route("/ask", methods=["POST"])
    def ask():
        user_input = request.json.get("question", "")
        answer = get_claude_response(user_input)
        return jsonify({"answer": answer})