from pages.Base_page import Base_page
from locators.All_locators import MainpageLocators

class Main_page(Base_page):
    
    locators = MainpageLocators()

    def Open_Keyboard(self):
        self.click_elem(self.locators.BUTTON_KEYBOARD)
        from pages.Main_page_with_keyboard import Main_page_with_keyboard
        return Main_page_with_keyboard(self.driver)

    def Open_Settings(self):
        self.click_elem(self.locators.BUTTON_SETINGS)
        from pages.Settings_page import Settings_page
        return Settings_page(self.driver)
    
