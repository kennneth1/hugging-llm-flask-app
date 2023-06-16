import os 
import joblib
from config import MODEL_CACHE_PATH, MODEL_FILE_PATH

def load_model():
    model = None
    # Check if the model file exists in the cache directory
    if os.path.exists(MODEL_FILE_PATH):
        # Load the model from the cache
        model = joblib.load(MODEL_FILE_PATH)
    else:
        # Download the model
        # Add your code here to download the model and save it to the cache directory
        # For example, using the Hugging Face Transformers library:
        # model = SomeDownloadFunction()
        
        # Save the downloaded model to the cache directory
        os.makedirs(MODEL_CACHE_PATH, exist_ok=True)
        joblib.dump(model, MODEL_FILE_PATH)