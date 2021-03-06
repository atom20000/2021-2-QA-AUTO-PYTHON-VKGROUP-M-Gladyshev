from selenium.webdriver.common.by import By

#Локаторы с главных страниц и из центральной панели
class Main_page():
    SPINER = (By.XPATH, '//div[contains(@class, "spinner_")]')
    OTHER_CORNER_BUTTON = (By.XPATH, '//div[contains(@class,"responseHead-module-burger")]')
    LOG_IN_BUTTON = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    OTHER_CENTRAL_BUTTON = (By.XPATH, '//li/span[contains(@class, "center-module-button")]')
    PROFILE_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/profile")]')
    AUDITORIUM_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/segments")]')
    TOOLS_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/tools")]')

#Локаторы из формы ввода
class LogIn_Form():
    LOG_IN_FORM = (By.XPATH,'//input[@name="email"]')
    PWD_FORM = (By.XPATH,'//input[@name="password"]')
    LOG_IN_BUTTON = (By.XPATH,'//div[contains(@class,"authForm-module-button")]')

#Локаторы для выхода из системы
class LogOut_Form():
    BUTTON_RIGHT_MODULE = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    BUTTON_LOG_OUT = (By.XPATH,'//li/a[contains(@href, "/logout")]')

#Локаторы из формы изменения контактной информации
class Contact_Form():
    FIO_FIELD=(By.XPATH,'//div[contains(@data-name, "fio")]//input')
    PHONE_FIELD = (By.XPATH, '//div[contains(@data-name, "phone")]//input')
    BUTTON_SAVE_CHANGE = (By.CLASS_NAME, "button__text")
