from pages.Base_page import Base_page
from locators.All_locators import MainPageLocators

class Main_page(Base_page):

    locators = MainPageLocators()

    def go_to_segment(self):
        self.click_elem(self.locators.AUDITORIUM_BUTTON)
        from pages.Segment_page import Segment_page
        return Segment_page(driver=self.driver)

    def go_to_dashboard(self):
        self.click_elem(self.locators.DASHBOARD_BUTTON)
        from pages.Dashboard_page import Dashboard_page
        return Dashboard_page(driver=self.driver)