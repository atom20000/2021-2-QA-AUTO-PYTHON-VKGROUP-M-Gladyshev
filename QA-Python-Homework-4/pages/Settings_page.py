from pages.Base_page import BasePage
from locators.All_locators import SettingsPageLocators
from pages.Source_news_page import SourceNewsPage
from pages.About_page import AboutPage
from pages.Main_page import MainPage

class SettingsPage(BasePage):

    locators = SettingsPageLocators()

    def go_to_source_news(self):
        self.scroll_by_element(method=self.swipe_up, locator_elem=self.locators.BUTTON_SOURCE_NEWS)
        self.click_elem(self.locators.BUTTON_SOURCE_NEWS)
        return SourceNewsPage(self.driver)
    
    def go_to_about(self):
        self.scroll_by_element(method=self.swipe_up, locator_elem=self.locators.BUTTON_ABOUT_APP)
        self.click_elem(self.locators.BUTTON_ABOUT_APP)
        return AboutPage(self.driver)
    
    def exit_settings(self):
        self.click_elem(self.locators.EXIT_SETTINGS)
        return MainPage(self.driver)