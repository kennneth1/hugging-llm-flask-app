from tkinter.messagebox import NO
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import (
    MODEL_NAME,
    NUM_BEAMS,
    NO_REPEAT_NGRAM_SIZE,
    MAX_LENGTH
)
import torch.cuda


class EndpointHandler():
    def __init__(self, model_name):
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"


def __call__(self, input_message):
        # Preprocess
        input_ids = self.tokenizer(input_message, return_tensors="pt").input_ids.to(device)
        # Forward
        output = self.model.generate(input_ids=input_ids, max_length=MAX_LENGTH, num_beams=NUM_BEAMS, no_repeat_ngram_size=NO_REPEAT_NGRAM_SIZE)
        # Postprocess
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)

        # Print the response as JSON
        print({"response": response})

        # Return the response as a dictionary
        return {"response": response}