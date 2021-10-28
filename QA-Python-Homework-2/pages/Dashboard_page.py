from pages.Main_page import Main_page
from locators.All_locators import DashboardPageLocators
import numpy
from PIL import Image
from utils.decorators import wait
import time
import os

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
        time.sleep(2)
        self.send_key(self.locators.FIELD_LINK, 'https://mail.ru/')
        time.sleep(2)
        self.send_key(self.locators.FIELD_NAME_COMPANY, name_company)
        self.click_elem(self.locators.FORMAT_BANNER_ADVERTISEMENT)
        #self.Generation_Image.save(name_company)
        self.driver.execute_script('arguments[0].style.display = "block";' , self.find_elem(self.locators.IMAGE_UPLOAD))
        time.sleep(2)

        print(os.path.abspath('maxresdefault.png'))
        time.sleep(2)
        import pdb; pdb.set_trace()
        self.send_key(self.locators.IMAGE_UPLOAD, '/mnt/g/Репозитории/2021-2-QA-AUTO-PYTHON-VKGROUP-M-Gladyshev/maxresdefault.png')
        time.sleep(2)
        self.click_elem(self.locators.SAVE_IMAGE)
        time.sleep(2)
        self.click_elem(self.locators.BUTTON_SAVE_ADVERTISEMENT)
        self.click_elem(self.locators.BUTTON_SAVE_COMPANY)

    @property
    def Generation_Image(self):
        return Image.fromarray((numpy.random.rand(100,100,3) * 255).astype('uint8')).convert('RGBA')