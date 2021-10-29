from pages.Base_page import Base_page
from pages.Login_page import Login_page
from locators.All_locators import StartPageLocators
import allure

class Start_page(Base_page):

    url = 'https://target.my.com/'
    
    locators =StartPageLocators()

    def go_to_login(self):
        self.check_button_not_hidden(self.locators.LOG_IN_BUTTON_MAIN, self.locators.OTHER_CORNER_BUTTON)
        with allure.step('Go to login page'):
            return Login_page(driver=self.driver)
