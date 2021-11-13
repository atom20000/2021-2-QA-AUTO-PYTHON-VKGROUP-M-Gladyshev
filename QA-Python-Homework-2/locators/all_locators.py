from selenium.webdriver.common.by import By

class BasicLocators():
    SPINER = (By.XPATH, '//div[contains(@class, "spinner_")]')

class StartPageLocators(BasicLocators):
    OTHER_CORNER_BUTTON = (By.XPATH, '//div[contains(@class,"responseHead-module-burger")]')
    LOG_IN_BUTTON_MAIN = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')

class AccountMyPageLocators(BasicLocators):
    MSG_ERROR_TITLE_LOGIN =(By.CLASS_NAME, 'formMsg_title')
    MSG_ERROR_TEXT_LOGIN = (By.CLASS_NAME, 'formMsg_text')
    
class LoginPageLocators(BasicLocators):
    LOG_IN_FORM = (By.XPATH,'//input[@name="email"]')
    PWD_FORM = (By.XPATH,'//input[@name="password"]')
    LOG_IN_BUTTON = (By.XPATH,'//div[contains(@class,"authForm-module-button")]')
    LOGIN_ERROR = (By.XPATH, '//div[contains(@class, "notify-module-content")]')

class MainPageLocators(BasicLocators):
    OTHER_CENTRAL_BUTTON = (By.XPATH, '//li/span[contains(@class, "center-module-button")]')
    PROFILE_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/profile")]')
    AUDITORIUM_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/segments")]')
    DASHBOARD_BUTTON = (By.XPATH, '//li/a[contains(@href, "/dashboard")]')
    TOOLS_BUTTON = (By.XPATH ,'//li/a[contains(@href, "/tools")]')

class SegmentsPageLocators(MainPageLocators):
    FIRST_PAGE_CREATE_BUTTON = (By.XPATH, '//a[contains(@href, "/segments/segments_list/new/")]')
    CHECKBOX_BUTTON = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    CREATE_SEGMENT_BUTTON = (By.XPATH, '//button[contains(@data-class-name, "Submit")]')
    ADD_NAME_SEGMENT = (By.XPATH, '//div[contains(@class, "segment-name")]//input[contains(@class, "input")]')
    CHOICE_VARIANT_SEGMENT = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    ADD_SEGMENT_BUTTON = (By.XPATH, f'//div[contains(@class, "adding-segments-modal__footer")]{CREATE_SEGMENT_BUTTON[1]}')
    LAST_PAGE_CREATE_BUTTON = (By.XPATH, f'//div[contains(@class, "create-button-wrap")]{CREATE_SEGMENT_BUTTON[1]}')
    TEMPLATE_NAME_SEGMENT =(By.XPATH, '//a[contains(@title, "{}")]')
    REMOVE_BUTTON = (By.XPATH, '//div[contains(@data-test, "remove-{}")]//span[contains(@class, "icon-cross")]')
    POP_UP_REMOVE_BUTTON = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')

class DashboardPageLocators(MainPageLocators):
    FIRST_PAGE_CREATE_BUTTON = (By.XPATH, '//a[contains(@href,"/campaign/new")]')
    CHOICE_TRAFFIC_BUTTON = (By.XPATH, '//div[contains(@class,"column-list-item _traffic")]')
    FIELD_LINK = (By.XPATH, '//input[contains(@data-gtm-id, "ad_url_text")]')
    FIELD_NAME_COMPANY = (By.XPATH, '//div[contains(@class, "nput__wrap")]//input[contains(@class, "input__inp") and not(@data-test)]')
    FORMAT_BANNER_ADVERTISEMENT = (By.XPATH, '//div[contains(@data-id, "patterns_banner")]')  
    IMAGE_UPLOAD = (By.XPATH, '//input[contains(@type,"file")and contains(@data-test, "image")]') #_240x400
    SAVE_IMAGE = (By.XPATH, '//input[contains(@class, "image-cropper")]')
    BUTTON_SAVE_ADVERTISEMENT = (By.XPATH, '//div[contains(@data-test, "submit_banner_button" )]')
    BUTTON_SAVE_COMPANY = (By.XPATH, '//div[contains(@class, "footer__button")]//button[contains(@data-class-name, "Submit")]')
    LAST_PAGE_CREATE_BUTTON = (By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]//div[contains(@data-test,"button")]')
    TEMPLATE_NAME_COMPANY = (By.XPATH, '//a[contains(@title, "{}")]')
    SETTINGS_BUTTON = (By.XPATH, '//div[contains(@data-test, "setting-{}")]//div[contains(@class, "icon-settings")]')
    REMOVE_BUTTON = (By.XPATH, '//li[contains(@data-test, "3") or contains(@title, "удалить")]')

class LogOut_Form(BasicLocators):
    BUTTON_RIGHT_MODULE = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    BUTTON_LOG_OUT = (By.XPATH,'//li/a[contains(@href, "/logout")]')

class Contact_Form(BasicLocators):
    FIO_FIELD=(By.XPATH,'//div[contains(@data-name, "fio")]//input')
    PHONE_FIELD = (By.XPATH, '//div[contains(@data-name, "phone")]//input')
    BUTTON_SAVE_CHANGE = (By.CLASS_NAME, "button__text")