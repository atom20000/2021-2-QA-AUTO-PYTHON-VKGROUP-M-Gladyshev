from pages.Base_page import Base_page
from pages.Main_page import Main_page
from locators.All_locators import LoginPageLocators

class Login_page(Base_page):

    locators = LoginPageLocators()

    def login(self, user, passwd):
        self.send_key(self.locators.LOG_IN_FORM, user)
        self.send_key(self.locators.PWD_FORM, passwd)
        self.click_elem(self.locators.LOG_IN_BUTTON)
        return Main_page(self.driver)
