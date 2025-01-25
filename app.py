from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route (this just shows a welcome message)
@app.route('/')
def home():
    return "Welcome to PetPal chatbot! How can I assist you?"

# Route for chatbot interaction
@app.route('/ask', methods=['POST'])
def ask():
    # Get user input from the JSON request
    user_input = request.json.get('message')
    
    # Simple logic for the chatbot (you can replace this with your AI logic)
    if user_input:
        # A simple response for now
        response = f"PetPal is here! You asked: {user_input}"
    else:
        response = "Please ask a question!"

    # Return the chatbot response as JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
