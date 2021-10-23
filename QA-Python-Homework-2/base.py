from _pytest.fixtures import FixtureRequest
from pages.Base_page import Base_page
import pytest
from fixtures import get_driver
from pages.Login_page import Login_page

class BaseCase():

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,driver, request: FixtureRequest):

        self.driver = driver
        
        self.start_page = request.getfixturevalue('start_page')
        
        #if self.authtorize:
        #    cookies = request.getfixturevalue('cookies_login')
        #    self.driver = request.getfixturevalue('driver')
        #    for cookie in cookies:
        #        self.driver.add_cookie(cookie)
        #    self.driver.refresh()
        #self.base_page: Base_page = request.getfixturevalue('base_page')
        