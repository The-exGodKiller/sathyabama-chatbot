from flask import Flask, render_template, request, jsonify
from chatbot_engine import generate_response, log_conversation


app = Flask(__name__)

@app.route("/")
def home():
    # Make sure you have 'index.html' in a 'templates' folder
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Safer way to get message, defaults to empty string if 'message' is missing
    user_input = request.json.get("message", "") 
    
    # Process request only if input is not empty
    if not user_input:
        return jsonify({"response": "Please enter a message."})

    response = generate_response(user_input)
    log_conversation(user_input, response)
    return jsonify({"response": response})

if __name__ == "__main__":
    # Use debug=True for local testing
    app.run(debug=True)
