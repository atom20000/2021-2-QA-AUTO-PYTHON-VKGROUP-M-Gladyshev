from locators.All_locators import SourceNewsPageLocators
from pages.Base_page import Base_page

class Source_news_page(Base_page):

    locators = SourceNewsPageLocators()
    
    def Retun_Settings(self):
        self.click_elem(self.locators.RETURN_SETTINGS)
        from pages.Settings_page import Settings_page
        return Settings_page(self.driver)