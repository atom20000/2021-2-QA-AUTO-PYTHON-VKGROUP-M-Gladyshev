from pages.Base_page import BasePage
from locators.All_locators import MainPagewithkeyboardLocators

class MainPageWithKeyboard(BasePage):

    locators = MainPagewithkeyboardLocators()

    def open_voice_input(self):
        self.click_elem(self.locators.BUTTON_INPUT_ACTION)
        from pages.Main_page import MainPage
        return MainPage(self.driver)
    
    def send_text(self,text):
        self.send_key(self.locators.FIELD_SEARCH, text)
        self.click_elem(self.locators.BUTTON_SEND_TEXT)
        