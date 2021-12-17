from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.all_locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    
    locators = RegistrationPageLocators()
    
    url = 'http://qa_myapp_proxy:8082/reg'

    def registration(self, username, emal, password, repassword, agree=True):
        self.send_key(self.locators.USERNAME_FIELD, username)
        self.send_key(self.locators.EMAIL_FIELD, emal)
        self.send_key(self.locators.PASSWORD_FIELD, password)
        self.send_key(self.locators.REPASSWORD_FIELD, repassword)
        if agree:
            self.click_elem(self.locators.ACCEPT_CHEKBOX)
        self.click_elem(self.locators.SUBMIT_BUTTON)
        #А если не пройдет ? написать переход к логину и проверку
        return MainPage(driver=self.driver)
        
    @property
    def error_message_text(self):
        return self.find_elem(self.locators.ERROR_MESSAGE).text
