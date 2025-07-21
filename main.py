from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENAI_KEY = os.getenv("OPENAI_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "Hello!")
    headers = {
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": user_input}]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
