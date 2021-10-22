from base import BaseCase
import pytest
import time

class TestClass(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        #time.sleep(5)
        assert self.driver.current_url == 'https://target.my.com/dashboard'