from base import BaseCase
from utils.decorators import *
from pages.dashboard_page import DashboardPage
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
        with allure.step('Check that the error message is displayed'):
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
        with allure.step('Check that the error message is displayed and switch page'):
            assert self.driver.current_url.find('https://account.my.com/login/') !=-1 
            assert page.find_elem(page.locators.MSG_ERROR_TITLE_LOGIN)
            assert page.find_elem(page.locators.MSG_ERROR_TEXT_LOGIN)

#@pytest.mark.skip('SKIP')
@allure.epic('Awesome PyTest framework')
@allure.feature('UI tests')
@allure.story('Segment tests')
@allure.testcase('Create segment test')
@pytest.mark.UI
def test_create_segment(temp_dir, logger, auto_main_page :DashboardPage):
    segment_page = auto_main_page.go_to_segment()
    segment_name = f'test_create_segment{time.time()}'
    segment_page.Create_segment(segment_name)
    with allure.step('Check that the segment create'):
        assert segment_page.Check_exist_segment(segment_name)
    segment_page.Remove_segment(segment_name)

#@pytest.mark.skip('SKIP')
@allure.epic('Awesome PyTest framework')
@allure.feature('UI tests')
@allure.story('Segment tests')
@allure.testcase('Remove segment test')
@pytest.mark.UI
def test_remove_segment(temp_dir, logger, auto_main_page :DashboardPage):
    segment_page = auto_main_page.go_to_segment()
    segment_name = f'test_remove_segment{time.time()}'
    segment_page.Create_segment(segment_name)
    segment_page.Remove_segment(segment_name)
    with allure.step('Check that the segment remove'):
        assert segment_page.Check_exist_segment(segment_name,exist=False)

#@pytest.mark.skip('SKIP')
@allure.epic('Awesome PyTest framework')
@allure.feature('UI tests')
@allure.story('Company tests')
@allure.testcase('Create company test')
@pytest.mark.UI
def test_create_campaign(temp_dir, logger, photo_dir, auto_main_page :DashboardPage):
    dashboard_page = auto_main_page
    campaign_name = f'test_create_company{time.time()}'
    dashboard_page.Create_campaign('https://mail.ru/', campaign_name, photo_dir)
    with allure.step('Check that the company create'):
        assert dashboard_page.Check_exist_campaign(campaign_name)
    dashboard_page.Remove_campaign(campaign_name)