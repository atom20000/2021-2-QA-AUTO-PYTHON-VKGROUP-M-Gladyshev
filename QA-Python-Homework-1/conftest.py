from selenium import webdriver
import pytest

executable_path = r'/usr/bin/chromedriver'
Login_mytarget = 'rarebe2161@wii999.com'
Pasword_mytarget = 'smB-g7E-rPu-TZ7'


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(executable_path)
    browser.get('https://target.my.com/')
    yield browser
    browser.close()
    
@pytest.fixture(scope='function')
def set_log_pwd():
    return (Login_mytarget,Pasword_mytarget)