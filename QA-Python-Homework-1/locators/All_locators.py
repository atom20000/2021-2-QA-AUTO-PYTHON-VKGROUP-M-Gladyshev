from selenium.webdriver.common.by import By
class Main_page():
    LOG_IN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')

class LogIn_Form():
    #LOG_IN_FORM = (By.XPATH,'//form/div/div/input[@name="email" and contains(text(),"authForm-module-input-3j70Dv")]')
    LOG_IN_FORM = (By.XPATH,'//input[@name="email"]')
    PWD_FORM = (By.XPATH,'//input[@name="password"]')
    LOG_IN_BUTTON = (By.XPATH,'//div[contains(@class,"authForm-module-button")]')