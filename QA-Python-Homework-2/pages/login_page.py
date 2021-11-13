from pages.base_page import BasePage
from locators.all_locators import LoginPageLocators
from pages.dashboard_page import DashboardPage
from pages.account_my_page import AccountMyPage
import allure

class LoginPage(BasePage):

    url = 'https://target.my.com/'

    locators = LoginPageLocators()

    def login(self, user, passwd):
        with allure.step("Logining....."):
            self.send_key(self.locators.LOG_IN_FORM, user)
            self.send_key(self.locators.PWD_FORM, passwd)
            self.click_elem(self.locators.LOG_IN_BUTTON)
        if self.driver.current_url == self.url:
            with allure.step('Remained on the same page'):
                return LoginPage(self.driver)
        elif self.driver.current_url.find(DashboardPage.url) !=-1:
            with allure.step('Go to dashboard page'):
                return DashboardPage(self.driver)
        elif self.driver.current_url.find(AccountMyPage.url) !=-1:
            with allure.step('Go to account.my page'):
                return AccountMyPage(self.driver)
