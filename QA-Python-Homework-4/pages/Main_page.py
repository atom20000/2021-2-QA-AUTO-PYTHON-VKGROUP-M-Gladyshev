from pages.base_page import BasePage
from locators.all_locators import MainpageLocators

class MainPage(BasePage):
    
    locators = MainpageLocators()

    def open_keyboard(self):
        self.click_elem(self.locators.BUTTON_KEYBOARD)
        from pages.main_page_with_keyboard import MainPageWithKeyboard
        return MainPageWithKeyboard(self.driver)

    def open_settings(self):
        self.click_elem(self.locators.BUTTON_SETINGS)
        from pages.settings_page import SettingsPage
        return SettingsPage(self.driver)
    
