from locators.All_locators import *
import time
from Base_class import BaseCase
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import pytest

#def Click(driver,locator):
#    elem = WebDriverWait(driver,5).until(EC.element_to_be_clickable(locator))
#    #driver.find_element(*locator)
#    elem.click()
#
class TestMain(BaseCase):
    def test_login(self,set_log_pwd):
        #driver.get('https://target.my.com/')
        self.login(set_log_pwd)
        time.sleep(5)