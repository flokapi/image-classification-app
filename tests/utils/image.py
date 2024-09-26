def load_image_bytes(image_path):
    with open(image_path, 'rb') as file:
        image_bytes = file.read()
    return image_bytes
