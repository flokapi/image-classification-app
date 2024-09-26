import socket
import os


class Settings():
    workdir: str
    local_test_port: int
    driver_path_path: str

    def __init__(self):
        self.workdir = os.getcwd()
        self.local_test_port = self.find_available_port()
        self.driver_path_path = ".driver_path"

    def find_available_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.listen(1)
            return s.getsockname()[1]


settings = Settings()


prediciton_set_1 = [
    ("data/happy/happy_1.jpg", "Happy"),
    ("data/happy/happy_3.jpg", "Happy"),
    ("data/happy/happy_7.jpg", "Happy"),
    ("data/sad/sad_1.jpg", "Sad"),
    ("data/sad/sad_2.jpg", "Sad"),
    ("data/sad/sad_3.png", "Sad"),
]
