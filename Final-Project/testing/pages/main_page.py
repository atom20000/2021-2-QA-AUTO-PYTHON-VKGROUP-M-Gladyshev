from pages.base_page import BasePage
from locators.all_locators import MainPageLocators


class MainPage(BasePage):

    locators = MainPageLocators()
    url = 'http://qa_myapp_proxy:8082/welcome/'

    def click_overlay(self,text_elem):
        self.click_elem((self.locators.OVERLAY_BUTTON[0],
            self.locators.OVERLAY_BUTTON[1].format(text_elem)))

    def click_navber(self, text_locator, text_locator_hide=None):
        if text_locator_hide is None:
            self.check_button_not_hidden(
                (self.locators.NAVBAR_BUTTON[0],self.locators.NAVBAR_BUTTON[1].format(text_locator))
            )
        else:
            self.check_button_not_hidden(
                (self.locators.NAVBAR_DROPLIST_BUTTON[0],self.locators.NAVBAR_DROPLIST_BUTTON[1].format(text_locator))
                (self.locators.NAVBAR_BUTTON[0], self.locators.NAVBAR_BUTTON[1].format(text_locator_hide))
            )

    def logout(self):
        self.click_elem(self.locators.LOGOUT_BUTTON)
        from login_page import LoginPage
        return LoginPage(driver= self.driver)