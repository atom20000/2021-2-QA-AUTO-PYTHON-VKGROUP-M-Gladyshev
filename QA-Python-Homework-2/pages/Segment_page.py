from pages.Main_page import Main_page
#from pages.Base_page import Base_page
from locators.All_locators import SegmentsPageLocators

class Segment_page(Main_page):
    locators = SegmentsPageLocators()

    def Create_segment(self,name_segment):
        if self.find_elem(self.locators.FIRST_PAGE_CREATE_BUTTON).is_displayed():
            self.click_elem(self.locators.FIRST_PAGE_CREATE_BUTTON)
        elif self.find_elem(self.locators.LAST_PAGE_CREATE_BUTTON).is_displayed():
            self.click_elem(self.locators.LAST_PAGE_CREATE_BUTTON)
        else: return False # Подумай еще раз 
        self.click_elem(self.locators.CHOICE_VARIANT_SEGMENT)
        self.click_elem(self.locators.CHECKBOX_BUTTON)
        self.click_elem(self.locators.ADD_SEGMENT_BUTTON)
        self.send_key(self.locators.ADD_NAME_SEGMENT,name_segment)
        self.click_elem(self.locators.CREATE_SEGMENT_BUTTON)

    def Remove_segment(self,name_segment):
        segment = self.find_elem((self.locators.TEMPLATE_NAME_SEGMENT[0],self.locators.TEMPLATE_NAME_SEGMENT[1].format(name_segment)))
        if segment:
            segment = segment.get_attribute("href")
            self.click_elem((self.locators.REMOVE_BUTTON[0], self.locators.REMOVE_BUTTON[1].format(segment[segment.rfind("/")+1:])))
            self.click_elem(self.locators.POP_UP_REMOVE_BUTTON)
            