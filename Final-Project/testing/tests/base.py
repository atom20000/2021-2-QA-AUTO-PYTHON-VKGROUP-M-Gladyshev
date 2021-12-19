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
        
    def _registration(self,agree=True, repassword=None,**kwargs):
        user = self.mysql_client.generate_user(**kwargs)
        registration_page = self.start_page.go_to_registration()
        page = registration_page.registration(
            username=user.username, 
            email=user.email, 
            password=user.password, 
            repassword=user.password if repassword is None else repassword,
            agree=agree)
        return page

class BaseAPITest():

    autologin = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, logger, request: FixtureRequest):
        self.logger = logger
        self.mock_client = request.getfixturevalue('mock_client')
        self.mysql_client = request.getfixturevalue('mysql_orm_client')
        if self.autologin:
            self.api_client = request.getfixturevalue('auto_login_API')
        else:
            self.api_client = request.getfixturevalue('api_client')

    def _registration(self, term='y', repassword=None, **kwargs):
        user = self.mysql_client.generate_user(**kwargs)
        response = self.api_client.registration(
            username=user.username, 
            email=user.email, 
            password=user.password, 
            repassword=user.password if repassword is None else repassword,
            term=term)
        return {'response':response, 'user':user}