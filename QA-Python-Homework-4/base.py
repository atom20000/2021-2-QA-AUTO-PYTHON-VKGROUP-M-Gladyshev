from _pytest.fixtures import FixtureRequest
from pages.Main_page import Main_page
import pytest

class Basecase():
    
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.main_page : Main_page = request.getfixturevalue('main_page')