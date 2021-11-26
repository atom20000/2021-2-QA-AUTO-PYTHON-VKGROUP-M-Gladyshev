from werkzeug.wrappers import request
from mock_server.mock import MockServer
from client.client import SocketClient
import settings
import pytest
import requests

def pytest_configure(config):
    config.Mock = MockServer(settings.MOCK_HOST,settings.MOCK_PORT)
    #вэйтер добавить

@pytest.fixture(scope='session')
def socket_client():
    return SocketClient(settings.MOCK_HOST,settings.MOCK_PORT)

def pytest_unconfigure(config):
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')
