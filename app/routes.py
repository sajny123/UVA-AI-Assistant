from app.services.claude_client import MCP
from flask import request, jsonify, render_template
import httpx, os

def setup_routes(app):
        
    @app.route('/health')
    def health():
        return jsonify({"status": "healthy"})

    @app.route("/api/ask", methods=["POST"])
    def ask():
        user_input = request.json.get("question", "")
        answer = MCP.ask_claude(user_input)
        
        try:
            n8n_url = os.environ.get('n8n_WEBHOOK_URL')
            data = {"question": user_input}, {"answer": answer}
            httpx.post(n8n_url, json=data)
            print("n8n connected")
        except Exception as e:
            print(f"An error occured while posting to n8n: {e}")

        return jsonify({"answer": answer})