from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, TimeoutException
import logging
import time


class BasePage():

    RETRY_CLICK = 4

    url = 'http://qa_myapp_proxy:8082'

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

    def wait_elem(self,timeout=None):
        if timeout is None: timeout=10
        return WebDriverWait(self.driver,timeout)

    def find_elem(self, locator, timeout=None):
        try:
            elem = self.wait_elem(timeout).until(EC.presence_of_element_located(locator))
            self.logger.info(f'Element found by locator : {locator[1]}')
            return elem
        except:
            self.logger.warning(f'Element not found by locator : {locator[1]}')
            raise

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

    def send_key(self, locator, key,timeout=None):
        elem = self.find_elem(locator,timeout)
        if self.wait_elem(timeout).until(EC.visibility_of(elem)):
            self.logger.info(f'Element is visible by locator: {locator[1]}')
            if elem.get_attribute('type') == 'text':
                elem.clear()
            elem.send_keys(key)
            self.logger.info("Send keys element by locator: {locator[1]}")
        else: self.logger.warning(f'Element is invisible by locator: {locator[1]}')

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    def check_button_not_hidden(self,locator,locator_hide_button=None):
        if self.find_elem(locator).is_displayed():
            self.click_elem(locator)
        else:
            self.action_chains.move_to_element(self.find_elem(locator_hide_button)).perform()
            self.click_elem(locator)

    def check_visibility_of_elem(self,locator, timeout=None):
        return self.wait_elem(timeout).until(EC.visibility_of_element_located(locator))

    def change_window(self,windows):
        try:
            self.wait_elem().until(EC.new_window_is_opened(windows))
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
        except TimeoutException:
            raise Exception("Page don't open separate window")
