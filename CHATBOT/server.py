from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt4all import GPT4All

app = Flask(__name__)
CORS(app)  # Allow React frontend to access API

model = GPT4All("mpt-7b-chat.Q4_0.gguf")



  # Change model if needed

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = model.generate(user_input, max_tokens=100)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
