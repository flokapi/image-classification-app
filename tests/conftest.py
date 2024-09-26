import pytest
import sys

import pprint


@pytest.hookimpl()
def pytest_unconfigure(config):
    reporter = config.pluginmanager.get_plugin('terminalreporter')
    sys.exit(reporter._session.exitstatus)
