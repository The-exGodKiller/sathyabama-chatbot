from flask import Flask, render_template, request, jsonify
from chatbot_engine import generate_response, log_conversation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = generate_response(user_input)
    log_conversation(user_input, response)
    return jsonify({"response": response})

if __name__ == "__main__":
    # Important: allow Render to bind to its provided host/port
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
