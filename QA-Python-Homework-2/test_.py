from base import BaseCase
import pytest
import time

class TestClass(BaseCase):
    
    #@pytest.mark.skip('SKIP')
    @pytest.mark.UI
    def test_login(self):
        time.sleep(5)
        assert self.driver.current_url == 'https://target.my.com/dashboard'

@pytest.mark.UI
def test_aut_log(auto_main_page):
    time.sleep(5)
    assert auto_main_page.driver.current_url == 'https://target.my.com/dashboard'