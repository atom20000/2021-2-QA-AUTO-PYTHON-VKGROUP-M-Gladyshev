from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators.all_locators import StartPageLocators
import allure

class StartPage(BasePage):

    url = 'https://target.my.com/'
    
    locators =StartPageLocators()

    def go_to_login(self):
        self.check_button_not_hidden(self.locators.LOG_IN_BUTTON_MAIN, self.locators.OTHER_CORNER_BUTTON)
        with allure.step('Go to login page'):
            return LoginPage(driver=self.driver)
