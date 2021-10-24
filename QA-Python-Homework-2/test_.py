from base import BaseCase
from utils.decorators import *
import pytest
import time

class TestClass(BaseCase):
    
    #@pytest.mark.skip('SKIP')
    @pytest.mark.UI
    def test_login_one(self):
        login_page = self.start_page.go_to_login()
        login_page.login('bhdg','gdfhjg') # МБ проверку на тип добавить
        assert wait(login_page.find_elem(login_page.locators.LOGIN_ERROR).is_displayed, check=True)
    #написать второй тест с переходом на страницу ошибки
    
    #@pytest.mark.skip('SKIP')
    @pytest.mark.UI
    def test_login_two(self):
        login_page = self.start_page.go_to_login()
        page = login_page.login('54534342','gdfhjg')
        assert self.driver.current_url.find('https://account.my.com/login/') !=-1
        assert page.find_elem(page.locators.MSG_ERROR_TITLE_LOGIN)
        assert page.find_elem(page.locators.MSG_ERROR_TEXT_LOGIN)

@pytest.mark.skip('SKIP')
@pytest.mark.UI
def test_aut_log(auto_main_page):
    time.sleep(5)
    assert auto_main_page.driver.current_url == 'https://target.my.com/dashboard'

