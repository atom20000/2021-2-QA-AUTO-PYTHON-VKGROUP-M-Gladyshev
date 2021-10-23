from pages.Base_page import Base_page
from pages.Login_page import Login_page
from locators.All_locators import StartPageLocators

class Start_page(Base_page):
    locators =StartPageLocators()

    def go_to_login(self):
        self.check_button_not_hidden(self.locators.LOG_IN_BUTTON_MAIN, self.locators.OTHER_CORNER_BUTTON)
        return Login_page(driver=self.driver)
