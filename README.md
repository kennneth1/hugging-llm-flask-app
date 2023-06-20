# Chatbot API

This is a minimalistic chatbot API built with Flask and HuggingFace's LLMs, that allows users to submit messages and receive responses via simple frontend.

## Features

- Serves as a starting point to further explore the development of chatbot APIs using Flask, Python, and language models
- Simple interface for one-off interactions with 1 of 2 LLMs (GPT2 or Dialo)


## Technologies Used

- Python
- Flask
- Docker
- GPT-2

## Important Considerations
Please note the following caveats regarding the current implementation:

- Limited Conversation History: Presently, the API does not retain a conversation history or support looping. Each interaction is treated as a one-off prompt, without referencing previous messages

- Latency Concerns: Due to the nature of the underlying model, lack of caching, and the computational requirements to support its tuning/inference, there may be excessive latency when receiving responses

## Getting Started

1. Clone the repository: `git clone https://github.com/kennneth1/hugging-llm-flask-app.git`
2. Navigate to root directory and initalize virtual env
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set env var, for MacOS: `export FLASK_APP=app.py`
5. Run the Flask application: `flask run`
6. Open your browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000`
7. Start chatting with the chatbot!

## Using Docker container
- docker build -t hugging-gpt2-flask-app .
- docker run -p 5000:5000 hugging-gpt2-flask-app

It is recommended to deploy to EC2 or ECS to support the high-compute inferencing needs.

## API Endpoints

- POST: `/api/gpt2-chatbot` or `/api/dialo-chatbot`: Send a user message to the chatbot and receives a response.

## Examples

### Sending a Message

After "Getting Started" or running your docker image, send message via terminal with:

`curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello"}' http://127.0.0.1:5000/api/gpt2-chatbot` or substitute gpt2 with a supported LLM of your choice.
