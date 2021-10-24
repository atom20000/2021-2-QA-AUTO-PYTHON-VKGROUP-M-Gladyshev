from webdriver_manager import driver
from pages.Base_page import Base_page
from pages.Segment_page import Segment_page
from locators.All_locators import MainPageLocators

class Main_page(Base_page):

    locators = MainPageLocators()

    def go_to_segment(self):
        self.click_elem(self.locators.AUDITORIUM_BUTTON)
        return Segment_page(driver=self.driver)