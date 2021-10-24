from pages.Main_page import Main_page
from locators.All_locators import SegmentsPageLocators

class Segment_page(Main_page):
    locators = SegmentsPageLocators()

    def Create_segment(self,name_segment):
        if self.find_elem(self.locators.FIRST_PAGE_CREATE_BUTTON):
            self.click_elem(self.locators.FIRST_PAGE_CREATE_BUTTON)
        elif self.find_elem(self.locators.LAST_PAGE_CREATE_BUTTON):
            self.click_elem(self.locators.LAST_PAGE_CREATE_BUTTON)
        else: return False # Подумай еще раз 
        self.click_elem(self.locators.CHECKBOX_BUTTON)
        self.click_elem(self.locators.ADD_SEGMENT_BUTTON)
        self.send_key(self.locators.ADD_NAME_SEGMENT,name_segment)
        self.click_elem(self.locators.CREATE_SEGMENT_BUTTON)
        