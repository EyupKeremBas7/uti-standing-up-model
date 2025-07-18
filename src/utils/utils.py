import os
import sys
import tensorflow as tf
from tensorflow.keras.models import load_model

def load_models():
    model = load_model("TrafficSignRecognition.pt")
    model.summary()
    return model