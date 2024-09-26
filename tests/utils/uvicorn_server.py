import uvicorn
from threading import Thread


class UvicornServer(Thread):
    port: int

    def __init__(self, _port):
        super().__init__()
        self.port = _port

    def run(self):
        uvicorn.run("app.main:app", host="127.0.0.1",
                    port=self.port, log_level="info")
