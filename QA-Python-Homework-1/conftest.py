from selenium import webdriver
import pytest

executable_path = r'/usr/bin/chromedriver'
Login_mytarget = 'rarebe2161@wii999.com'
Pasword_mytarget = 'smB-g7E-rPu-TZ7'

New_FIO = 'gdhgdl'
New_Phone = '79359-35352'

#Фикстура по созданию экземпляра драйвера
@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(executable_path)
    browser.maximize_window()
    browser.get('https://target.my.com/')
    yield browser
    browser.close()
    
#Фикстура по установки логина и пароля для входа
@pytest.fixture(scope='function')
def set_log_pwd():
    return (Login_mytarget,Pasword_mytarget)

#Фикстура по установки ФИО и телефона для изменения контактной информации
@pytest.fixture(scope='function')
def set_contact_inf():
    return (New_FIO, New_Phone)
