import base64
import numpy as np
import cv2


# def binary_to_base64(binary_img):
#     return base64.b64encode(binary_img).decode("utf-8")


def resize_image_with_aspect_ratio(image, desired_width: int):
    (h, w) = image.shape[:2]
    r = desired_width / float(w)
    dim = (desired_width, int(h * r))

    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def binary_to_base64(binary_img):
    np_array = np.frombuffer(binary_img, np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    # resize = cv2.resize(img, (256, 256))
    img = resize_image_with_aspect_ratio(img, desired_width=500)
    _, buffer = cv2.imencode('.jpg', img)
    image_bytes = buffer.tobytes()
    return base64.b64encode(image_bytes).decode("utf-8")
