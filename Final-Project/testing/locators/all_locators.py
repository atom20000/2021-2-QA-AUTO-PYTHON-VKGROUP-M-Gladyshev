from selenium.webdriver.common.by import By

class BaseLoginPageLocators():
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'submit')
    ERROR_MESSAGE = (By.ID, 'flash')

class LoginPageLocators(BaseLoginPageLocators):
    CREATE_USER_BUTTON = (By.XPATH, '//a[contains(@href,"/reg")]')

class RegistrationPageLocators(BaseLoginPageLocators):
    EMAIL_FIELD = (By.ID, 'email')
    REPASSWORD_FIELD = (By.ID, 'confirm')
    ACCEPT_CHEKBOX = (By.ID, 'term')
    LOGIN_BUTTON = (By.XPATH, '//a[contains(@href,"/login")]')

class MainPageLocators():
    LOGOUT_BUTTON = (By.XPATH, '//a[contains(@href,"/logout")]')
    LOGIN_NAME = (By.XPATH, '//div[contains(@id,"login-name")]//li[contains(text(),"Logged as {}")]')
    VK_ID = (By.XPATH, '//div[contains(@id,"login-name")]//li[contains(text(),"VK ID: {}")]')
    