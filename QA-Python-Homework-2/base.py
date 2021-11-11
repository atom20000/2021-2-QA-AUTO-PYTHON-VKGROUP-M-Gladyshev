from _pytest.fixtures import FixtureRequest
from pages.Start_page import Start_page
import pytest

class BaseCase():

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver,logger, request: FixtureRequest):

        self.driver = driver
        self.start_page : Start_page = request.getfixturevalue('start_page')
        