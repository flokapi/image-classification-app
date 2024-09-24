import subprocess
import atexit
import time


from tests.config import settings


PORT = settings.local_test_port


uvicorn_ps = None


def start():
    global uvicorn_ps
    uvicorn_ps = subprocess.Popen(
        ["uvicorn", "app.main:app", "--port", f"{PORT}", "--reload"])
    time.sleep(0.5)


def stop():
    if uvicorn_ps:
        uvicorn_ps.terminate()
        uvicorn_ps.wait(timeout=5)

        if uvicorn_ps.poll() is not None:
            uvicorn_ps.kill()


atexit.register(stop)
