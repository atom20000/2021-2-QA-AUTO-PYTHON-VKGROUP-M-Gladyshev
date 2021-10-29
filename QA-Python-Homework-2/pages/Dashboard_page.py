from pages.Main_page import Main_page
from locators.All_locators import DashboardPageLocators
from utils.Generation_Image import Generation_Image
import os
import allure

class Dashboard_page(Main_page):

    url = 'https://target.my.com/dashboard'

    locators = DashboardPageLocators()

    
    def Create_company(self, url, name_company, photo_dir):
        if self.check_access_button_create(self.locators.FIRST_PAGE_CREATE_BUTTON, 3):
            self.click_elem(self.locators.FIRST_PAGE_CREATE_BUTTON)
        elif self.check_access_button_create(self.locators.LAST_PAGE_CREATE_BUTTON, 3):
            self.click_elem(self.locators.LAST_PAGE_CREATE_BUTTON)
        else: return False
        self.click_elem(self.locators.CHOICE_TRAFFIC_BUTTON)
        self.send_key(self.locators.FIELD_LINK, url)
        self.send_key(self.locators.FIELD_NAME_COMPANY, name_company)
        self.click_elem(self.locators.FORMAT_BANNER_ADVERTISEMENT)
        photo = os.path.join(photo_dir,f'{name_company}.png')
        with allure.step('Save generation image'):
            Generation_Image().save(photo)
        self.driver.execute_script('arguments[0].style.display = "block";' , self.find_elem(self.locators.IMAGE_UPLOAD))
        self.send_key(self.locators.IMAGE_UPLOAD, photo)
        self.click_elem(self.locators.BUTTON_SAVE_ADVERTISEMENT)
        self.click_elem(self.locators.BUTTON_SAVE_COMPANY)

    def Remove_company(self, name_company):
        company = self.find_elem((self.locators.TEMPLATE_NAME_COMPANY[0], self.locators.TEMPLATE_NAME_COMPANY[1].format(name_company)))
        if company:
            company = company.get_attribute("href")
            self.click_elem((self.locators.SETTINGS_BUTTON[0], self.locators.SETTINGS_BUTTON[1].format(company[company.rfind("/")+1:company.rfind("?")])))
            self.click_elem(self.locators.REMOVE_BUTTON)
        
    def check_access_button_create(self,locator, timeout=None):
        try:
            if self.find_elem(locator,timeout):
                if self.find_elem(locator,timeout).is_displayed():
                    return True
        except: return False