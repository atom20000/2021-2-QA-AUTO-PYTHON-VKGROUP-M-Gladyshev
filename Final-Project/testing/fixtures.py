from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage 
from pages.main_page import MainPage
from clients.clent_db.client_mysql import MySQLORMClient
from clients.client_app import AppClient
from clients.client_mock import MockClient
import logging
import pytest
import allure
import faker


@pytest.fixture
def start_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture(scope='session')
def cookies_login():
    browser = get_driver()
    browser.get('QA_myapp:8080/login') 
    LoginPage(browser).login()
    cookies = browser.get_cookies()
    browser.quit()
    
    return cookies

@pytest.fixture(scope='function')
def auto_main_page(cookies_login, driver):
    for cookie in cookies_login:
        driver.add_cookie(cookie)
    driver.refresh()
    with allure.step('Cookies added'):
        return MainPage(driver=driver)

#Фикстура по созданию экземпляра драйвера
@pytest.fixture(scope='function')
def driver():
    browser = get_driver()
    #проверить доступ к app
    browser.get('http://QA_myapp:8080')
    with allure.step('Create driver'):
        yield browser
    with allure.step('Quite driver'):
        browser.quit()

def get_driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    capabilites = {
        'browserName':'chrome',
        'version':'96.0'
    }
    #проверить доступ к селеноид
    browser = webdriver.Remote(f'http://selenoid:4444/wd/hub',options=options, desired_capabilities=capabilites)
    browser.maximize_window()
    return browser

@pytest.fixture(scope='session')
def mysql_orm_client():
    client = MySQLORMClient(user='test_qa', password='qa_test')
    client.connect()
    yield client
    client.connection.close()

@pytest.fixture(scope='session')
def api_client():
    return AppClient('http://QA_myapp:8080')

@pytest.fixture(scope='session')
def mock_client():
    return MockClient('http://VK_mock:8080')

