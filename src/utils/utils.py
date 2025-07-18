import os
import sys
import tensorflow as tf
from tensorflow.keras.models import load_model

def load_models():
    model_path = os.path.join(os.path.dirname(__file__), '../../storage/Trafic_signs_model_8.keras')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
    
    model = load_model(model_path)
    model.summary()
    return model