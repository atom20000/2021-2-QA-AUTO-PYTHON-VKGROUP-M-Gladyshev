from mock_server.mock import *
from client.client import SocketClient
import settings
import pytest
import requests
import logging
import time
import os
import shutil

def pytest_configure(config):
    root_path = os.path.abspath(os.path.join(os.getcwd(),'data'))
    if not hasattr(config, 'workerinput'):
        if os.path.exists(root_path):
            shutil.rmtree(root_path)
        os.mkdir(root_path)
        flask_redirect_stderr(os.path.join(root_path, 'flask.log'))
        flask_redirect_stdout(os.path.join(root_path, 'flask_out.log'))
        run_server()
        wait_ready(settings.MOCK_HOST,settings.MOCK_PORT)
    config.base_temp_dir = root_path
    #И логер

@pytest.fixture(scope='session')
def socket_client():
    return SocketClient(settings.MOCK_HOST,settings.MOCK_PORT)

def pytest_unconfigure():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')

def wait_ready(host, port, timeout=5):
    started = False
    st = time.time()
    while time.time() - st <= timeout:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except requests.exceptions.ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 5s!')


@pytest.fixture(scope='session')
def logger(request):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(request.config.base_temp_dir, 'client.log')
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, "w")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('client')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()
    