from pages.Base_page import Base_page
from locators.All_locators import SettingsPageLocators
from pages.Source_news_page import Source_news_page
from pages.About_page import About_page
from pages.Main_page import Main_page

class Settings_page(Base_page):

    locators = SettingsPageLocators()

    def Go_to_Source_News(self):
        self.scroll_by_element(method=self.swipe_up, locator_elem=self.locators.BUTTON_SOURCE_NEWS)
        self.click_elem(self.locators.BUTTON_SOURCE_NEWS)
        return Source_news_page(self.driver)
    
    def Go_to_About(self):
        self.scroll_by_element(method=self.swipe_up, locator_elem=self.locators.BUTTON_ABOUT_APP)
        self.click_elem(self.locators.BUTTON_ABOUT_APP)
        return About_page(self.driver)
    
    def Exit_Settings(self):
        self.click_elem(self.locators.EXIT_SETTINGS)
        return Main_page(self.driver)