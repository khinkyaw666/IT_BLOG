from flask import Flask, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I assist you?",
    "password": "Ensure your password is at least 12 characters long!",
    "malware": "Install reliable antivirus software to prevent threats.",
    "default": "I'm here to help! Ask me anything."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response = responses.get(user_message, responses["default"])
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
