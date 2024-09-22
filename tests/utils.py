import subprocess


def load_image_bytes(image_path):
    with open(image_path, 'rb') as file:
        image_bytes = file.read()
    return image_bytes


def start_uvicorn():
    command = ["uvicorn", "app.main:app",
               "--host", "127.0.0.1", "--port", "8000"]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process


def stop_uvicorn(process):
    process.terminate()
    process.wait()
