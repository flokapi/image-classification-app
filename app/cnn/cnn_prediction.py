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


def read_image_from_bytes(image_bytes):
    np_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)[:, :, 0]
    cv2.imwrite("out.png", img)
    img = img.reshape((1, IMAGE_SIZE_X, IMAGE_SIZE_Y, 1))
    return img


def initialize():
    global model
    model = tf.keras.models.load_model(MODEL_PATH)


def predict(file_content):
    print(model)

    img = read_image_from_bytes(file_content)
    print("========================== img read")
    prediction = model.predict(img)
    print("========================== prediction done")
    print(prediction)
    result = int(np.argmax(prediction))
    print("========================== result found")
    print(result)

    return result
