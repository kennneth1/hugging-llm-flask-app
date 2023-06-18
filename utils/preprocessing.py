from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import jsonify 
import re


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

    # Return the response as a dictionary
    return {"response": response}

def remove_metadata(response):
    """Removes metadata from the response."""
    pattern = r"\{.*?\}"
    cleaned_response = re.sub(pattern, "", response)
    return cleaned_response.strip()

def remove_repetition(response):
    """Removes repeated phrases from the response."""
    cleaned_response = re.sub(r"(\b\w+\b)(?=.*\b\1\b)", "", response, flags=re.IGNORECASE)
    return cleaned_response.strip()

def clean_response(response):
    # Remove repeated characters
    cleaned_response = re.sub(r'(\w)\1+', r'\1', response)

    # Remove consecutive punctuation marks
    cleaned_response = re.sub(r'([.,!?])\1+', r'\1', cleaned_response)

    # Remove leading/trailing spaces and punctuation marks
    cleaned_response = cleaned_response.strip(' .,!?')

    # Capitalize the first letter
    cleaned_response = cleaned_response.capitalize()

    return cleaned_response