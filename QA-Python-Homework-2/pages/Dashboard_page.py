from pages.Main_page import Main_page
from locators.All_locators import DashboardPageLocators
import numpy
from PIL import Image

class Dashboard_page(Main_page):

    locators = DashboardPageLocators()

    
    def Create_company(self, name_company):
        #if self.find_elem(self.locators.FIRST_PAGE_CREATE_BUTTON).is_displayed():
        #    self.click_elem(self.locators.FIRST_PAGE_CREATE_BUTTON)
        #elif self.find_elem(self.locators.LAST_PAGE_CREATE_BUTTON).is_displayed():
        #    self.click_elem(self.locators.LAST_PAGE_CREATE_BUTTON)
        #else: return False # Подумай еще раз а надо ли оно тебе
        self.click_elem(self.locators.LAST_PAGE_CREATE_BUTTON) # Удалить починить If
        self.click_elem(self.locators.CHOICE_TRAFFIC_BUTTON)
        self.send_key(self.locators.FIELD_LINK, 'mail.ru')
        self.send_key(self.locators.FIELD_NAME_COMPANY, name_company)
        self.click_elem(self.locators.FORMAT_BANNER_ADVERTISEMENT)
        #self.Generation_Image.save(name_company)
        self.send_key(self.locators.IMAGE_UPLOAD,'maxresdefault.jpg')
        self.click_elem(self.locators.SAVE_IMAGE)
        self.click_elem(self.locators.BUTTON_SAVE_ADVERTISEMENT)
        self.click_elem(self.locators.BUTTON_SAVE_COMPANY)

    @property
    def Generation_Image(self):
        return Image.fromarray((numpy.random.rand(100,100,3) * 255).astype('uint8')).convert('RGBA')