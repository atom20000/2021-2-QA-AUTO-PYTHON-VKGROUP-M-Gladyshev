from selenium.webdriver.support import expected_conditions
from locators.All_locators import *
import time
from Base_class import BaseCase
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import pytest

#def Click(driver,locator):
#    elem = WebDriverWait(driver,5).until(EC.element_to_be_clickable(locator))
#    #driver.find_element(*locator)
#    elem.click()
#
class TestClass(BaseCase):

    @pytest.mark.skip("SKIP")
    @pytest.mark.UI
    def test_login(self,set_log_pwd):
        self.login(set_log_pwd)
        assert self.find_elem(Main_page.USER_NAME_RIGHT_MODULE).is_displayed()
        #assert self.find_elem(Main_page.USER_NAME_RIGHT_MODULE).get_attribute('title') == set_log_pwd[0]
        time.sleep(5)

    @pytest.mark.skip("SKIP")
    @pytest.mark.UI
    def test_logout(self,set_log_pwd):
        self.login(set_log_pwd)
        time.sleep(5) #Напиши проверку что страница загружена
        self.click_elem(LogOut_Form.BUTTON_RIGHT_MODULE)
        time.sleep(5) #Напиши проверку что всплывашка полностью вышла
        self.click_elem(LogOut_Form.BUTTON_LOG_OUT)
        assert self.find_elem(Main_page.LOG_IN_BUTTON).is_displayed()
        time.sleep(5)

    @pytest.mark.skip("SKIP")
    @pytest.mark.UI
    def test_contact(self,set_log_pwd):
        self.login(set_log_pwd)
        try:
            self.click_elem(Main_page.PROFILE_BUTTON)
        except:
            self.click_elem(Main_page.OTHER_CENTRAL_BUTTON)
            self.click_elem(Main_page.PROFILE_BUTTON)
        self.send_key(Contact_Form.FIO_FIELD,'dhgfhj')
        self.send_key(Contact_Form.PHONE_FIELD,'79403')
        self.click_elem(Contact_Form.BUTTON_SAVE_CHANGE)
        #assert self.find_elem(Contact_Form.NOTIFICATION_SUCCESS).is_displayed()
        #assert self.find_elem(Contact_Form.FIO_FIELD) =='dhgfhj' 
        #Допилить проверку что сохранения прошло
        time.sleep(5)