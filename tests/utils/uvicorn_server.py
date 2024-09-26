import uvicorn
from subprocess import Popen
import time


class UvicornServer():
    port: int

    def __init__(self, _port):
        super().__init__()
        self.port = _port

    def start(self):
        cmd = ["uvicorn", "app.main:app", "--port", f"{self.port}"]
        self.ps = Popen(cmd)
        time.sleep(1)

    def stop(self):
        self.ps.terminate()
        time.sleep(1)
