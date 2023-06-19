from flask import Flask, request, render_template
from utils.preprocessing import clean_response, load_model, chat
import os

app = Flask(__name__)

# cold load the model and tokenizer
model, tokenizer = load_model()

templates_dir = os.path.join(os.getcwd(), "app", "templates")
app.template_folder = templates_dir

@app.route("/")
def index():
    return render_template("index.html")
    
# Handle POST requests to the custom chatbot endpoint
@app.route("/api/custom-endpoint", methods=["POST"])
def chatbot():
    # Get the input message from the request
    
    input_message = request.json["message"]
    print("Received message:", input_message)

    # Return response
    response = chat(input_message)
    response = response.get("response", "")  # Extract the "response" value
    print("Generated response:", response)

    response = clean_response(response, input_message)
    print("Cleaned response:", response)

    return response

# Handle POST requests to hugging face's inference endpoint
@app.route("/api/hugging-endpoint", methods=["POST"])
def chatbot_with_hugging():
    return "404: Not yet implemented"

# Run the Flask application
if __name__ == "__main__":
    app.run(port=5000)