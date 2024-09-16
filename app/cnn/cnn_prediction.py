import time
import cv2
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

from app.config import settings


TF_MODEL_FILE_NAME = settings.tf_model_file_name
STATIC_FILES_LOCATION = settings.static_files_location
IMAGE_SIZE_X = settings.image_size_x
IMAGE_SIZE_Y = settings.image_size_y

MODEL_PATH = Path(STATIC_FILES_LOCATION).joinpath(TF_MODEL_FILE_NAME)

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
        value = "Sad"
    else:
        value = "Happy"
    return {"value": value, "yhat": float(yhat)}
