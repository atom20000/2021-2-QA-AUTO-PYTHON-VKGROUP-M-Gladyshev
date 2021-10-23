from selenium import webdriver
import pytest
from Static_var import *

#Фикстура по созданию экземпляра драйвера
@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(EXECUTABLE_PATH)
    browser.maximize_window()
    browser.get('https://target.my.com/')
    yield browser
    browser.close()
    
#Фикстура по установки логина и пароля для входа
@pytest.fixture(scope='function')
def set_log_pwd():
    return {'LOGIN' : LOGIN_MYTARGET, 'PWD' : PASSWORD_MYTARGET}

#Фикстура по установки ФИО и телефона для изменения контактной информации
@pytest.fixture(scope='function')
def set_contact_inf():
    return {'FIO' : NEW_FIO, 'PHONE' : NEW_PHONE}
