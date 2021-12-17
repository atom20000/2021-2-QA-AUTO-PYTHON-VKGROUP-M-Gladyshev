import logging
from _pytest.fixtures import FixtureRequest
import pytest

class BaseUITest():

    autologin = True
    
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger, request: FixtureRequest):
        self.driver = driver
        self.logger = logger
        self.mock_client = request.getfixturevalue('mock_client')
        self.mysql_client = request.getfixturevalue('mysql_orm_client')
        if self.autologin:
            self.start_page = request.getfixturevalue('auto_main_page')
        else:
            self.start_page = request.getfixturevalue('start_page')
        
#self.api_client = request.getfixturevalue('api_client')