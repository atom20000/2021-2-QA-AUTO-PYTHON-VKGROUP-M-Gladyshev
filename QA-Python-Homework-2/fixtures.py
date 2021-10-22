from selenium import webdriver
from pages.Base_page import Base_page
from pages.Login_page import Login_page
import pytest

@pytest.fixture
def base_page(driver):
    return Base_page(driver=driver)

@pytest.fixture(scope='session')
def cookies_login():
    browser = get_driver()
    browser.get('https://target.my.com/')
    Login_page(browser).login('rarebe2161@wii999.com','smB-g7E-rPu-TZ7')
    cookies = browser.get_cookies()
    browser.quit()
    return cookies


#Фикстура по созданию экземпляра драйвера
@pytest.fixture(scope='function')
def driver():
    browser = get_driver()
    browser.get('https://target.my.com/')
    yield browser
    browser.quit()

# Переделать через менеджер драйвера
def get_driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser