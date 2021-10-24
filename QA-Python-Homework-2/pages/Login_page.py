from pages.Base_page import Base_page
from pages.Main_page import Main_page
from pages.Account_my_page import Account_my_page
from locators.All_locators import LoginPageLocators

class Login_page(Base_page):

    url = 'https://target.my.com/'

    locators = LoginPageLocators()

    def login(self, user, passwd):
        self.send_key(self.locators.LOG_IN_FORM, user)
        self.send_key(self.locators.PWD_FORM, passwd)
        self.click_elem(self.locators.LOG_IN_BUTTON)
        if self.driver.current_url == self.url:
            return Main_page(self.driver)
        elif self.driver.current_url.find(Account_my_page.url) !=-1:
            return Account_my_page(self.driver)
