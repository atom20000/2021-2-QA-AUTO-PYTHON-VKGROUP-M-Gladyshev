from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.All_locators import *
import pytest

class BaseCase:

    driver = None

    RETRY_CLICK=3

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,driver):
        self.driver = driver   

    def wait_elem(self,timeout=None):
        if timeout is None: timeout=5
        return WebDriverWait(self.driver,timeout)

    def find_elem(self, locator, timeout=None):
        self.wait_elem(timeout).until(EC.invisibility_of_element_located(Main_page.SPINER))
        return self.wait_elem(timeout).until(EC.presence_of_element_located(locator))
    
    def click_elem(self, locator, timeout=None):
        for i in range(self.RETRY_CLICK):
            try:
                elem = self.find_elem(locator,timeout)
                elem = self.wait_elem(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except:
                if i==self.RETRY_CLICK-1: raise

    def send_key(self,locator,key,timeout=None):
        elem = self.find_elem(locator,timeout)
        elem.clear()
        elem.send_keys(key)

    def check_button_not_hidden(self,locator,locator_hide_button):
        if self.find_elem(locator).is_displayed():
            self.click_elem(locator)
        else:
            self.click_elem(locator_hide_button)
            self.click_elem(locator)

    def login(self,set_log_pwd):
        self.check_button_not_hidden(Main_page.LOG_IN_BUTTON, Main_page.OTHER_CORNER_BUTTON)
        self.send_key(LogIn_Form.LOG_IN_FORM,set_log_pwd[0])
        self.send_key(LogIn_Form.PWD_FORM,set_log_pwd[1])
        self.click_elem(LogIn_Form.LOG_IN_BUTTON)

    def logout(self):
        self.click_elem(LogOut_Form.BUTTON_RIGHT_MODULE)
        #time.sleep(5) #Напиши проверку что всплывашка полностью вышла
        self.click_elem(LogOut_Form.BUTTON_LOG_OUT)