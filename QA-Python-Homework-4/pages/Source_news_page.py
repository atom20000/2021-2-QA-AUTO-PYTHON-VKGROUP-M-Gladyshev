from locators.all_locators import SourceNewsPageLocators
from pages.base_page import BasePage

class SourceNewsPage(BasePage):

    locators = SourceNewsPageLocators()
    
    def retun_settings(self):
        self.click_elem(self.locators.RETURN_SETTINGS)
        from pages.settings_page import SettingsPage
        return SettingsPage(self.driver)