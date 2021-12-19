from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage 
from pages.main_page import MainPage
from clients.client_db.client_mysql import MySQLORMClient
from clients.client_app import AppClient
from clients.client_mock import MockClient
import logging
import pytest
import allure


@pytest.fixture
def start_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture(scope='session')
def cookies_login(mysql_orm_client):
    browser = get_driver()
    browser.get('http://qa_myapp_proxy:8082/login') 
    user = mysql_orm_client.generate_user()
    mysql_orm_client.insert_row(user)
    LoginPage(browser).login(username=user.username, password=user.password)
    cookies = browser.get_cookies()
    browser.quit()
    return cookies

@pytest.fixture(scope='function')
def auto_main_page(cookies_login, driver):
    for cookie in cookies_login:
        driver.add_cookie({
            'name': cookie.get('name'),
            'value': cookie.get('value')
        })
    driver.refresh()
    with allure.step('Cookies added'):
        return MainPage(driver=driver)

@pytest.fixture(scope='function')
def driver():
    browser = get_driver()
    browser.get('http://qa_myapp_proxy:8082/login')
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
def auto_login_API(mysql_orm_client):
    user = mysql_orm_client.generate_user()
    mysql_orm_client.insert_row(user)
    Api = AppClient('http://qa_myapp_proxy:8082')
    Api.login(username=user.username,password=user.password)
    return Api

@pytest.fixture(scope='function')
def api_client():
    return AppClient('http://qa_myapp_proxy:8082')

@pytest.fixture(scope='session')
def mock_client():
    return MockClient('http://vk_mock:8080')

