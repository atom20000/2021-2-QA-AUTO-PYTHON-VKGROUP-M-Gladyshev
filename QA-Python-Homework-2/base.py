from _pytest.fixtures import FixtureRequest
from pages.Start_page import Start_page
import pytest

class BaseCase():

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver,logger, request: FixtureRequest):

        self.driver = driver
        #self.logger = logger
        self.start_page : Start_page = request.getfixturevalue('start_page')
        
        #if self.authtorize:
        #    cookies = request.getfixturevalue('cookies_login')
        #    self.driver = request.getfixturevalue('driver')
        #    for cookie in cookies:
        #        self.driver.add_cookie(cookie)
        #    self.driver.refresh()
        #self.base_page: Base_page = request.getfixturevalue('base_page')
        