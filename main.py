from flask import Flask, request, jsonify
from utils.preprocessing import load_model


app = Flask(__name__)

# cold load the model and tokenizer
model, tokenizer = load_model()

# Define a route for generating responses
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get the input message from the request
    input_message = request.json["message"]

    # Tokenize the input message
    input_ids = tokenizer.encode(input_message, return_tensors="pt")

    # Generate a response from the model
    output = model.generate(input_ids, max_length=100)

    # Decode the generated response
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Print the response as JSON
    print({"response": response})

    # Return the response as JSON
    return jsonify({"response": response})

# Run the Flask application
if __name__ == "__main__":
    app.run()