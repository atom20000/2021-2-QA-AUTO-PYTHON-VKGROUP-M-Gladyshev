from pages.Base_page import BasePage
from locators.All_locators import MainpageLocators

class MainPage(BasePage):
    
    locators = MainpageLocators()

    def open_keyboard(self):
        self.click_elem(self.locators.BUTTON_KEYBOARD)
        from pages.Main_page_with_keyboard import MainPageWithKeyboard
        return MainPageWithKeyboard(self.driver)

    def open_settings(self):
        self.click_elem(self.locators.BUTTON_SETINGS)
        from pages.Settings_page import SettingsPage
        return SettingsPage(self.driver)
    
