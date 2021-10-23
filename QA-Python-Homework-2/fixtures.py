from selenium import webdriver
from pages.Start_page import Start_page 
from pages.Main_page import Main_page
import pytest

@pytest.fixture
def start_page(driver):
    return Start_page(driver=driver)

@pytest.fixture(scope='session')
def cookies_login():
    browser = get_driver()
    browser.get('https://target.my.com/')
    Start_page(browser).go_to_login().login('rarebe2161@wii999.com','smB-g7E-rPu-TZ7')
    cookies = browser.get_cookies()
    browser.quit()
    return cookies

@pytest.fixture(scope='function')
def auto_main_page(cookies_login, driver):
    for cookie in cookies_login:
        driver.add_cookie(cookie)
    driver.refresh()
    return Main_page(driver=driver)

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