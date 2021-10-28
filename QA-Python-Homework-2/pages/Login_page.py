from pages.Base_page import Base_page
from locators.All_locators import LoginPageLocators
from pages.Dashboard_page import Dashboard_page
from pages.Account_my_page import Account_my_page

class Login_page(Base_page):

    url = 'https://target.my.com/'

    locators = LoginPageLocators()

    def login(self, user, passwd):
        self.send_key(self.locators.LOG_IN_FORM, user)
        self.send_key(self.locators.PWD_FORM, passwd)
        self.click_elem(self.locators.LOG_IN_BUTTON)
        if self.driver.current_url == self.url:
            from pages.Start_page import Start_page
            return Start_page(self.driver)
        elif self.driver.current_url.find(Dashboard_page.url) !=-1:
            return Dashboard_page(self.driver)
        elif self.driver.current_url.find(Account_my_page.url) !=-1:
            return Account_my_page(self.driver)
