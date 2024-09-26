import pytest
import os
import signal


@pytest.hookimpl()
def pytest_unconfigure(config):
    os.kill(os.getpid(), signal.SIGTERM)
