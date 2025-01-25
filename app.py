from flask import Flask, request, jsonify

app = Flask(__name__)

# Chatbot logic
def petpal_chatbot(user_input):
    responses = {
        "How often should I groom my cat": "You should groom your cat once or twice a week.",
        "What should I feed my dog": "Feed your dog high-quality dog food suitable for their size and age.",
        "How can I train my pet": "Use positive reinforcement with treats and patience.",
    }
    return responses.get(user_input, "I'm sorry, I don't have an answer to that.")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    reply = petpal_chatbot(user_message)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
