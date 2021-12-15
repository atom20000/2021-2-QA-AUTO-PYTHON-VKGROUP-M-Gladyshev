from base_page import BasePage
from main_page import MainPage
from locators.all_locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    
    def __init__(self):
        self.url = self.url+'/reg'
        self.locators = RegistrationPageLocators()

    def registration(self, username, emal, password, repassword, agree=True):
        self.send_key(self.locators.USERNAME_FIELD, username)
        self.send_key(self.locators.EMAIL_FIELD, emal)
        self.send_key(self.locators.PASSWORD_FIELD, password)
        self.send_key(self.locators.REPASSWORD_FIELD, repassword)
        if agree:
            self.click_elem(self.locators.ACCEPT_CHEKBOX)
        self.click_elem(self.locators.SUBMIT_BUTTON)
        return MainPage(driver=self.driver)

