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

1. Clone the repository: `git clone https://github.com/your-username/chatbot-api.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python main.py`
4. Open your browser and navigate to `http://localhost:5000`
5. Start chatting with the chatbot!

## API Endpoints

- `POST /api/chatbot`: Sends a user message to the chatbot and receives a response.

## Examples

### Sending a Message

Handles POST request to `/api/chatbot` with the following JSON payload:

```json
{
  "message": "Hello, chatbot!"
}

{
  "response": "Hi there! How can I assist you today?"
}




