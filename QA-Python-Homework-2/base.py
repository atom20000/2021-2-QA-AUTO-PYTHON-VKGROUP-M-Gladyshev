from _pytest.fixtures import FixtureRequest
from pages.start_page import StartPage
import pytest

class BaseCase():

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver,logger, request: FixtureRequest):

        self.driver = driver
        self.start_page : StartPage = request.getfixturevalue('start_page')
        