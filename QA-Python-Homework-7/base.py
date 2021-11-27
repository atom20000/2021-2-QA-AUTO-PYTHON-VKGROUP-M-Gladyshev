from client.client import SocketClient
import pytest


class BaseCase():

    @pytest.fixture(scope='session',autouse=True)
    def setup(self, socket_client):
        self.client : SocketClient = socket_client