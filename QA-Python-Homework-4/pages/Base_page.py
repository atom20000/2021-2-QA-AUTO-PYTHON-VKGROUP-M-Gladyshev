from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
from appium.webdriver.common.touch_action import TouchAction
from locators.All_locators import BasicLocators

class Base_page():

    RETRY_CLICK = 4

    locators = BasicLocators()

    def __init__(self,driver):
        self.driver = driver
        
    #Функция создания экземпляра WebDriverWait
    def wait_elem(self,timeout=None):
        if timeout is None: timeout=10
        return WebDriverWait(self.driver,timeout)

    #Функция по поиску элемента на странице
    def find_elem(self, locator, timeout=None):
        return self.wait_elem(timeout).until(EC.presence_of_element_located(locator))

    #Функция по нажатию на элемент
    def click_elem(self, locator, timeout=None):
        for i in range(self.RETRY_CLICK):
            try:
                elem = self.find_elem(locator,timeout)
                elem = self.wait_elem(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException,
             ElementClickInterceptedException, 
             ElementNotInteractableException,):
                if i==self.RETRY_CLICK-1: raise

    #Функция по отправлению данных в поля ввода
    def send_key(self, locator, key,timeout=None):
        elem = self.find_elem(locator,timeout)
        if elem.get_attribute('type') == 'text':
            elem.clear()
        elem.send_keys(key)
    
    def scroll_element_left(self, locator, right_x):
        element = self.find_elem(locator)
        left_x = element.location['x']
        middle_y = (element.location['y']*2 + element.rect['height']) / 2
        action = TouchAction(self.driver)
        action. \
            press(x=right_x, y=middle_y). \
            wait(ms=200). \
            move_to(x=left_x, y=middle_y). \
            release(). \
            perform()
    def scroll_carousel_by_element_to_left(self,locator_carousel,locator_elem,right_x):
        while len(self.driver.find_elements(*locator_elem)) == 0:
            self.scroll_element_left(locator_carousel,right_x)
#int(self.driver.get_window_size()['wigth']/2)
