from client.client import SocketClient
from utils.builder import *
import pytest
import json


class BaseCase():

    @pytest.fixture(scope='function',autouse=True)
    def setup(self, socket_client):
        self.client : SocketClient = socket_client
        self.user_data = user_data()

    def status_code_from_response(self,response):
        return int(response[0].split()[1])
    
    def body_from_response(self,response):
        return json.loads(response[-1])
