from pages.Base_page import Base_page
from locators.All_locators import MainPagewithkeyboardLocators

class Main_page_with_keyboard(Base_page):

    locators = MainPagewithkeyboardLocators()

    def Open_voice_input(self):
        self.click_elem(self.locators.BUTTON_INPUT_ACTION)
        from pages.Main_page import Main_page
        return Main_page(self.driver)
    
    def Send_text(self,text):
        self.send_key(self.locators.FIELD_SEARCH, text)
        self.click_elem(self.locators.BUTTON_SEND_TEXT)
        