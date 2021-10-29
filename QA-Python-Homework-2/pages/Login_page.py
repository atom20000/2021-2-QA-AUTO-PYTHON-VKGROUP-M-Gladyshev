from pages.Base_page import Base_page
from locators.All_locators import LoginPageLocators
from pages.Dashboard_page import Dashboard_page
from pages.Account_my_page import Account_my_page
import allure

class Login_page(Base_page):

    url = 'https://target.my.com/'

    locators = LoginPageLocators()

    def login(self, user, passwd):
        self.send_key(self.locators.LOG_IN_FORM, user)
        self.send_key(self.locators.PWD_FORM, passwd)
        self.click_elem(self.locators.LOG_IN_BUTTON)
        if self.driver.current_url == self.url:
            with allure.step('Remained on the same page'):
                return Login_page(self.driver)
        elif self.driver.current_url.find(Dashboard_page.url) !=-1:
            with allure.step('Go to dashboard page'):
                return Dashboard_page(self.driver)
        elif self.driver.current_url.find(Account_my_page.url) !=-1:
            with allure.step('Go to account.my page'):
                return Account_my_page(self.driver)
