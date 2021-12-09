from locators.All_locators import SourceNewsPageLocators
from pages.Base_page import BasePage

class SourceNewsPage(BasePage):

    locators = SourceNewsPageLocators()
    
    def retun_settings(self):
        self.click_elem(self.locators.RETURN_SETTINGS)
        from pages.Settings_page import SettingsPage
        return SettingsPage(self.driver)