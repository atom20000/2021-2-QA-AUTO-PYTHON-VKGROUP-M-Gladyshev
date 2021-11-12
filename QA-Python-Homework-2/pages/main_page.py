from pages.base_page import BasePage
from locators.all_locators import MainPageLocators
import allure

class MainPage(BasePage):

    locators = MainPageLocators()

    def go_to_segment(self):
        self.click_elem(self.locators.AUDITORIUM_BUTTON)
        with allure.step('Go to segment page'):
            from pages.segment_page import SegmentPage
            return SegmentPage(driver=self.driver)

    def go_to_dashboard(self):
        self.click_elem(self.locators.DASHBOARD_BUTTON)
        with allure.step('Go to dashboard page'):
            from pages.dashboard_page import DashboardPage
            return DashboardPage(driver=self.driver)
        