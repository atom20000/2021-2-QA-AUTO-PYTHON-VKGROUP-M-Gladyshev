from mock_server.mock import *
from client.client import SocketClient
import settings
import pytest
import requests

def pytest_configure():
    run_server()
    #вэйтер добавить

@pytest.fixture(scope='session')
def socket_client():
    return SocketClient(settings.MOCK_HOST,settings.MOCK_PORT)

def pytest_unconfigure():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')
