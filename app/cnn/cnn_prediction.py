import time
import cv2
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

from app.config import settings


MODEL_PATH = settings.tf_model_path
IMAGE_SIZE_X = settings.image_size_x
IMAGE_SIZE_Y = settings.image_size_y

model = None


def initialize():
    global model
    model = tf.keras.models.load_model(MODEL_PATH)


def predict(file_content):
    np_array = np.frombuffer(file_content, np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    resize = tf.image.resize(img, (IMAGE_SIZE_X, IMAGE_SIZE_Y))
    yhat = model.predict(np.expand_dims(resize/255, 0))[0][0]
    if yhat > 0.5:
        classification = "Sad"
    else:
        classification = "Happy"
    return {"classification": classification, "value": float(yhat)}
