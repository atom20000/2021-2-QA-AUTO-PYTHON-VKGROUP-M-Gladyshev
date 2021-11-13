from numpy import True_
from pages.main_page import MainPage
from locators.all_locators import SegmentsPageLocators
import allure

class SegmentPage(MainPage):

    url = 'https://target.my.com/segments/'

    locators = SegmentsPageLocators()

    def Create_segment(self,name_segment):
        with allure.step('Segment creating...'):
            if self.find_elem(self.locators.FIRST_PAGE_CREATE_BUTTON).is_displayed():
                self.click_elem(self.locators.FIRST_PAGE_CREATE_BUTTON)
            elif self.find_elem(self.locators.LAST_PAGE_CREATE_BUTTON).is_displayed():
                self.click_elem(self.locators.LAST_PAGE_CREATE_BUTTON)
            else: return False 
            self.click_elem(self.locators.CHOICE_VARIANT_SEGMENT)
            self.click_elem(self.locators.CHECKBOX_BUTTON)
            self.click_elem(self.locators.ADD_SEGMENT_BUTTON)
            self.send_key(self.locators.ADD_NAME_SEGMENT,name_segment)
            self.click_elem(self.locators.CREATE_SEGMENT_BUTTON)

    def Remove_segment(self,name_segment):
        with allure.step('Segment removing...'):
            segment = self.find_elem((self.locators.TEMPLATE_NAME_SEGMENT[0],self.locators.TEMPLATE_NAME_SEGMENT[1].format(name_segment)))
            if segment:
                segment = segment.get_attribute("href")
                self.click_elem((self.locators.REMOVE_BUTTON[0], self.locators.REMOVE_BUTTON[1].format(segment[segment.rfind("/")+1:])))
                self.click_elem(self.locators.POP_UP_REMOVE_BUTTON)

    def Check_exist_segment(self,segment_name,exist=True,timeout=None):
        if exist:
            return self.find_elem((self.locators.TEMPLATE_NAME_SEGMENT[0],self.locators.TEMPLATE_NAME_SEGMENT[1].format(segment_name)),timeout)
        else:
            return self.check_invisibility_of_elem((self.locators.TEMPLATE_NAME_SEGMENT[0],self.locators.TEMPLATE_NAME_SEGMENT[1].format(segment_name)),timeout)