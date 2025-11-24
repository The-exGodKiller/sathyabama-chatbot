from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables (needed for GEMINI_API_KEY)
load_dotenv()

# Import chatbot logic
from chatbot_engine import generate_response, log_conversation

# Configure Flask
app = Flask(__name__, static_folder="static", template_folder="templates")

# Enable CORS so frontend fetch() works everywhere
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "❓ Please enter a valid message."})

    response = generate_response(user_input)
    log_conversation(user_input, response)
    return jsonify({"response": response})

if __name__ == "__main__":
    # Never use debug=True on Render
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
