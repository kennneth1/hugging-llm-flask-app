from flask import Flask, request, render_template
from utils.custom_preprocessing import clean_response, load_model, chat
import os

app = Flask(__name__)

templates_dir = os.path.join(os.getcwd(), "app", "templates")
app.template_folder = templates_dir

@app.route("/")
def index():
    return render_template("index.html")
    
# Handle POST requests to gpt2 endpoint
@app.route("/api/gpt2-chatbot", methods=["POST"])
def gpt2_chatbot():
    # Get the input message from the request
    input_message = request.json["message"]
    print("Received message:", input_message)

    # Return response
    response = chat(input_message, "gpt2-medium")
    response = response.get("response", "")  # Extract the "response" value
    print("Generated response:", response)

    response = clean_response(response, input_message)
    print("Cleaned response:", response)

    return response

# Handle POST requests to dialo endpoint
@app.route("/api/dialo-chatbot", methods=["POST"])
def dialo_chatbot():
    # Get the input message from the request
    input_message = request.json["message"]
    print("Received message:", input_message)

    # Return response
    response = chat(input_message, "microsoft/DialoGPT-medium")
    response = response.get("response", "")  # Extract the "response" value
    print("Generated response:", response)

    response = clean_response(response, input_message)
    print("Cleaned response:", response)

    return response

# Run the Flask application
if __name__ == "__main__":
    app.run(port=5000)