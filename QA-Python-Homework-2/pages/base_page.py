import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, TimeoutException
from locators.all_locators import BasicLocators
import time


class BasePage():

    RETRY_CLICK = 4

    locators = BasicLocators()

    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def is_opened(self,timeout=10):
        start = time.time()
        while time.time()-start < timeout:
            if self.driver.current_url.find(self.url) != -1:
                self.logger.info(f"Page:{self.url} is opened")
                return True
        self.logger.warning(f"Page:{self.url} isn't opened")
        raise 

    #Функция создания экземпляра WebDriverWait
    def wait_elem(self,timeout=None):
        if timeout is None: timeout=10
        return WebDriverWait(self.driver,timeout)

    #Функция по поиску элемента на странице
    def find_elem(self, locator, timeout=None):
        self.wait_elem(timeout).until(EC.invisibility_of_element_located(self.locators.SPINER))
        try:
            elem = self.wait_elem(timeout).until(EC.presence_of_element_located(locator))
            self.logger.info(f'Element found by locator : {locator[1]}')
            return elem
        except:
            self.logger.warning(f'Element not found by locator : {locator[1]}')
            return False
    #Функция по нажатию на элемент
    def click_elem(self, locator, timeout=None):
        for i in range(self.RETRY_CLICK):
            try:
                elem = self.find_elem(locator,timeout)
                elem = self.wait_elem(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                self.logger.info(f'Click element by locator : {locator[1]}')
                return
            except (StaleElementReferenceException,
             ElementClickInterceptedException, 
             ElementNotInteractableException,
             TimeoutException):
                if i==self.RETRY_CLICK-1: 
                    self.logger.warning(f'Not Click element by locator : {locator[1]};\n {Exception}')
                    raise

    #Функция по отправлению данных в поля ввода
    def send_key(self, locator, key,timeout=None):
        elem = self.find_elem(locator,timeout)
        if self.wait_elem(timeout).until(EC.visibility_of(elem)):
            self.logger.info(f'Element is visible by locator: {locator[1]}')
            if elem.get_attribute('type') == 'text':
                elem.clear()
            elem.send_keys(key)
            self.logger.info("Send keys element by locator: {locator[1]}")
        else: self.logger.warning(f'Element is invisible by locator: {locator[1]}')

    #Функция по проверке, что кнопка не скрыта в меню (Если окно маленького размера)
    def check_button_not_hidden(self,locator,locator_hide_button):
        if self.find_elem(locator).is_displayed():
            self.click_elem(locator)
        else:
            self.click_elem(locator_hide_button)
            self.click_elem(locator)

    def check_invisibility_of_elem(self,locator, timeout=None):
        return self.wait_elem(timeout).until(EC.invisibility_of_element_located(locator))
