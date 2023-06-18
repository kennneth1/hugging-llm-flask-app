# Chatbot API

This is a minimalistic chatbot API built with Flask and HuggingFace's GPT-2 LLM, that allows users to submit messages and receive responses via simple frontend.

## Features

- Simple interface for interacting with the chatbot
- Engage in one-off Q and A's with the chatbot using the API
- Serves as a starting point to further explore the development of chatbot APIs using Flask, Python, and language models

## Technologies Used

- Python
- Flask
- Docker
- GPT-2

## Important Considerations
Please note the following caveats regarding the current implementation:

- Limited Conversation History: Presently, the API does not retain a conversation history or support looping. Each interaction is treated as a one-off prompt, without referencing previous messages

- Latency Concerns: Due to the nature of the underlying model and the computational requirements to support its tuning, there may be excessive latency when receiving responses. We are continuously working to optimize and enhance the API's performance

## Getting Started

1. Clone the repository: `git clone https://github.com/kennneth1/hugging-llm-flask-app.git`
2. Navigate to root directory and initalize virtual env
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set env var, for MacOS: `export FLASK_APP=main.py`
5. Run the Flask application: `flask run`
6. Open your browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000`
7. Start chatting with the chatbot!

## Using Docker container
- docker build -t hugging-gpt2-flask-app .
- docker run -p 5000:5000 hugging-gpt2-flask-app

It is recommended to deploy to EC2 or ECS to support the high-compute inferencing needs.

## API Endpoints

- POST: `/api/chatbot`: Send a user message to the chatbot and receives a response.

## Examples

### Sending a Message

After "Getting Started" or running your docker image, send message to `/api/chatbot` via terminal with the command:

`curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello"}' http://127.0.0.1:5000/api/chatbot`
