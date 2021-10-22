from _pytest.fixtures import FixtureRequest
from pages.Base_page import Base_page
import pytest
from fixtures import get_driver
from pages.Login_page import Login_page

class BaseCase():

    driver = None

    authtorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,driver, request: FixtureRequest):

        self.driver = driver


        self.base_page: Base_page = request.getfixturevalue('base_page')
        #Login_page(self.driver).login('rarebe2161@wii999.com','smB-g7E-rPu-TZ7')
        if self.authtorize:
            for cookie in request.getfixturevalue('cookies_login'):
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        