import os 
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import jsonify 
import torch 

from config import (
    MODEL_NAME, 
)

def load_model():
    # Download the model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    
    return model, tokenizer

def chat(input_message):
    # Load model and tokenizer 
    model, tokenizer = load_model()

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
