from appium import webdriver
from Static_var import *
import pytest

@pytest.fixture(scope='function')
def driver():
    browser = get_driver(URL_ANDROID,CAPABILITY)
    yield browser
    browser.quit()

# Переделать через менеджер драйвера
def get_driver(url,capability):
    browser = webdriver.Remote(url,desired_capabilities=capability)
    return browser