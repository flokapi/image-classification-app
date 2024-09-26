import subprocess
import atexit
import time


import asyncio
import uvicorn
import threading
from tests.config import settings
import signal


PORT = settings.local_test_port


# uvicorn_ps = None


# def start():
#     global uvicorn_ps
#     uvicorn_ps = subprocess.Popen(
#         ["uvicorn", "app.main:app", "--port", f"{PORT}"])
#     time.sleep(0.5)


# def stop():
#     if uvicorn_ps:
#         uvicorn_ps.terminate()
#         uvicorn_ps.wait(timeout=5)

#         if uvicorn_ps.poll() is not None:
#             uvicorn_ps.kill()


# atexit.register(stop)


def start_uvicorn():
    uvicorn.run("app.main:app", host="127.0.0.1", port=PORT, log_level="info")


def start():
    uvicorn_thread = threading.Thread(target=start_uvicorn)
    uvicorn_thread.start()


def stop():
    pass
