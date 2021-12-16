from _pytest.fixtures import FixtureRequest
import pytest

class BaseUITest():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,driver,request: FixtureRequest):
        self.driver = driver
        self.api_client = request.getfixturevalue('api_client')
        self.mock_client = request.getfixturevalue('mock_client')
        self.mysql_client = request.getfixturevalue('mysql_orm_client')
        self.start_page = request.getfixturevalue('start_page')
        