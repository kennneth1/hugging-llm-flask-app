# Chatbot API

This is a simple chatbot API built with Flask and HuggingFace's GPT-2 LLM, that allows users to submit messages and receive responses.

## Features

- Provides a user-friendly interface for interacting with the chatbot
- Supports real-time conversation with the chatbot - one-off prompts, retention of prior messages is not yet implemented
- Handles various user queries and provides relevant responses

## Technologies Used

- Python
- Flask
- HTML
- JavaScript
- jQuery

## Getting Started

1. Clone the repository: `git clone https://github.com/kennneth1/hugging-llm-flask-app.git`
2. Navigate to root directory and initalize virtual env
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set env var, for MacOS: `export FLASK_APP=main.py`
5. Run the Flask application: `python main.py`
6. Open your browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000`
7. Start chatting with the chatbot!

- docker build -t hugging-gpt2-flask-app .
- docker run -p 5000:5000 hugging-gpt2-flask-app


## API Endpoints

- `POST /api/chatbot`: Sends a user message to the chatbot and receives a response.

## Examples

### Sending a Message

Handles POST request to `/api/chatbot` via terminal with this command:
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello"}' http://127.0.0.1:5000/api/chatbotwith 

Or with the following JSON payload:

```json
{
  "message": "Hello, chatbot!"
}

{
  "response": "Hi there! How can I assist you today?"
}




