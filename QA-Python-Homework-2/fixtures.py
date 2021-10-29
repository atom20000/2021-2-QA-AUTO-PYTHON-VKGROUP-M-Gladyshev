from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.Start_page import Start_page 
from pages.Dashboard_page import Dashboard_page
from Static_var import *
import logging
import pytest
import allure

@pytest.fixture
def start_page(driver):
    return Start_page(driver=driver)

@pytest.fixture(scope='session')
def cookies_login():
    browser = get_driver()
    browser.get('https://target.my.com/') # Проверку натип мб надо 
    Start_page(browser).go_to_login().login(LOGIN_MYTARGET,PASSWORD_MYTARGET)
    cookies = browser.get_cookies()
    browser.quit()
    
    return cookies

@pytest.fixture(scope='function')
def auto_main_page(cookies_login, driver):
    for cookie in cookies_login:
        driver.add_cookie(cookie)
    driver.refresh()
    with allure.step('Cookies added'):
        return Dashboard_page(driver=driver)

#Фикстура по созданию экземпляра драйвера
@pytest.fixture(scope='function')
def driver():
    browser = get_driver()
    browser.get('https://target.my.com/')
    with allure.step('Create driver'):
        yield browser
    with allure.step('Quite driver'):
        browser.quit()

# Переделать через менеджер драйвера
def get_driver():
    browser = webdriver.Chrome(ChromeDriverManager(version='latest',log_level=logging.CRITICAL).install())
    browser.maximize_window()
    return browser

