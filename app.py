from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
import os

app = Flask(__name__)

# 🔑 setează cheia ta OpenAI în variabila de mediu
# (în terminal: export OPENAI_API_KEY="cheia_ta" sau pe Windows: setx OPENAI_API_KEY "cheia_ta")
client = OpenAI(api_key="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")
print(os.getenv("OPENAI_KEY"))
@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # 🔮 Aici se generează răspunsul cu GPT
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Ești un asistent empatic de sănătate mintală, numit MindEase."},
            {"role": "user", "content": user_message}
        ]
    )

    ai_message = response.choices[0].message.content
    return jsonify({"reply": ai_message})

if __name__ == "__main__":
    app.run(debug=True)
