from selenium.webdriver.common.by import By


class Main_page():
    OTHER_CORNER_BUTTON = (By.CLASS_NAME, 'responseHead-module-burger-1u0Lts')
    LOG_IN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    USER_NAME_RIGHT_MODULE = (By.CLASS_NAME, 'right-module-userNameWrap-3Odw2D')
    OTHER_CENTRAL_BUTTON = (By.XPATH, '//li/span')
    PROFILE_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/profile")]')
    AUDITORIUM_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/segments")]')
    TOOLS_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/tools")]')

class LogIn_Form():
    LOG_IN_FORM = (By.XPATH,'//input[@name="email"]')
    PWD_FORM = (By.XPATH,'//input[@name="password"]')
    LOG_IN_BUTTON = (By.XPATH,'//div[contains(@class,"authForm-module-button")]')

class LogOut_Form():
    BUTTON_RIGHT_MODULE = (By.XPATH, '//div[contains(@class, "right-module-rightButton-3e-duF")]')
    BUTTON_LOG_OUT = (By.XPATH,'//li/a[contains(@href, "/logout")]')

class Contact_Form():
    FIO_FIELD=(By.XPATH,'//div[contains(@data-name, "fio")]//input')
    PHONE_FIELD = (By.XPATH, '//div[contains(@data-name, "phone")]//input')
    BUTTON_SAVE_CHANGE = (By.XPATH,'//button[contains(@data-class-name, "Submit")]//div[contains(@class, "button__text")]')
    NOTIFICATION_SUCCESS = (By.XPATH, '//div[contains(@data-class-name, "SuccessView")]')
