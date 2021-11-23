from appium import webdriver
from static_var import *
from pages.main_page import MainPage
import pytest

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def driver():
    browser = get_driver(URL_ANDROID,CAPABILITY)
    yield browser
    browser.quit()

# Переделать через менеджер драйвера
def get_driver(url,capability):
    browser = webdriver.Remote(url,desired_capabilities=capability)
    return browser