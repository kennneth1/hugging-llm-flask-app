import os 
from transformers import AutoModelForCausalLM, AutoTokenizer

from config import (
    MODEL_NAME, 
)

def load_model():
    # Download the model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    
    return model, tokenizer