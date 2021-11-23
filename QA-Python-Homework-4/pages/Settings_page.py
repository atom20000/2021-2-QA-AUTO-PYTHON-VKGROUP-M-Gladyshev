from pages.base_page import BasePage
from locators.all_locators import SettingsPageLocators
from pages.source_news_page import SourceNewsPage
from pages.about_page import AboutPage
from pages.main_page import MainPage

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