from client.client import SocketClient
from utils.builder import *
import logging
import pytest
import json


class BaseCase():

    @pytest.fixture(scope='function',autouse=True)
    def setup(self, socket_client, logger):
        self.client : SocketClient = socket_client
        self.user_data = user_data()
        self.logger = logging.getLogger('client')

    def status_code_from_response(self,response):
        return int(response[0].split()[1])
    
    def body_from_response(self,response):
        return json.loads(response[-1])
    
    def hendler_response(self, response):
        self.logger.info(f'{response[0].split()[1]} {response[1:-2]} {response[-1]}')
