from flask import Flask, request, jsonify
from chatbot import load_dataset, get_answer

app = Flask(__name__)

# Load the dataset
dataset = load_dataset("dataset.txt")

@app.route('/chat', methods=['POST'])
def chat():
    """API endpoint to get chatbot responses."""
    user_message = request.json.get("message")
    response = get_answer(user_message, dataset)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0") 
