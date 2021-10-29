from base import BaseCase
from utils.decorators import *
from pages.Dashboard_page import Dashboard_page
import pytest
import time
import allure

class TestClass(BaseCase):
    #@pytest.mark.skip('SKIP')
    @allure.epic('Awesome PyTest framework')
    @allure.feature('UI tests')
    @allure.story('Negative log in tests')
    @allure.testcase('First test')
    @pytest.mark.UI
    def test_login_one(self,temp_dir,logger):
        login_page = self.start_page.go_to_login()
        login_page.login('bhdg','gdfhjg') # МБ проверку на тип добавить
        assert wait(login_page.find_elem(login_page.locators.LOGIN_ERROR).is_displayed, check=True) #Можно сделать через встроенный wait
    
    #@pytest.mark.skip('SKIP')
    @allure.epic('Awesome PyTest framework')
    @allure.feature('UI tests')
    @allure.story('Negative log in tests')
    @allure.testcase('Second test')
    @pytest.mark.UI
    def test_login_two(self, temp_dir,logger):
        login_page = self.start_page.go_to_login()
        page = login_page.login('54534342','gdfhjg')
        assert self.driver.current_url.find('https://account.my.com/login/') ==-1 #!!!!!!!!!!!!!!!!!!!!!
        assert page.find_elem(page.locators.MSG_ERROR_TITLE_LOGIN)
        assert page.find_elem(page.locators.MSG_ERROR_TEXT_LOGIN)

#@pytest.mark.skip('SKIP')
@allure.epic('Awesome PyTest framework')
@allure.feature('UI tests')
@allure.story('Segment tests')
@allure.testcase('Create segment test')
@pytest.mark.UI
def test_create_segment(temp_dir, logger, auto_main_page :Dashboard_page):
    segment_page = auto_main_page.go_to_segment()
    segment_name = f'test_create_segment{time.time()}'
    segment_page.Create_segment(segment_name)
    assert segment_page.find_elem((segment_page.locators.TEMPLATE_NAME_SEGMENT[0],segment_page.locators.TEMPLATE_NAME_SEGMENT[1].format(segment_name)))
    segment_page.Remove_segment(segment_name)

#@pytest.mark.skip('SKIP')
@allure.epic('Awesome PyTest framework')
@allure.feature('UI tests')
@allure.story('Segment tests')
@allure.testcase('Remove segment test')
@pytest.mark.UI
def test_remove_segment(temp_dir, logger, auto_main_page :Dashboard_page):
    segment_page = auto_main_page.go_to_segment()
    segment_name = f'test_remove_segment{time.time()}'
    segment_page.Create_segment(segment_name)
    segment_page.Remove_segment(segment_name)
    assert segment_page.check_invisibility_of_elem((segment_page.locators.TEMPLATE_NAME_SEGMENT[0],segment_page.locators.TEMPLATE_NAME_SEGMENT[1].format(segment_name)))

#@pytest.mark.skip('SKIP')
@allure.epic('Awesome PyTest framework')
@allure.feature('UI tests')
@allure.story('Company tests')
@allure.testcase('Create company test')
@pytest.mark.UI
def test_create_company(temp_dir, logger, photo_dir, auto_main_page :Dashboard_page):
    dashboard_page = auto_main_page
    company_name = f'test_create_company{time.time()}'
    dashboard_page.Create_company('https://mail.ru/', company_name, photo_dir)
    assert dashboard_page.find_elem((dashboard_page.locators.TEMPLATE_NAME_COMPANY[0],dashboard_page.locators.TEMPLATE_NAME_COMPANY[1].format(company_name)))
    dashboard_page.Remove_company(company_name)

#@pytest.mark.skip('SKIP')
#@pytest.mark.UI
#def test_aut_log(auto_main_page):
#    time.sleep(5)
#    assert auto_main_page.driver.current_url == 'https://target.my.com/dashboard'

