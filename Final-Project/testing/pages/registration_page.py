from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.all_locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    
    locators = RegistrationPageLocators()
    
    url = 'http://qa_myapp_proxy:8082/reg'

    def registration(self, username, email, password, repassword, agree=True):
        self.send_key(self.locators.USERNAME_FIELD, username)
        self.send_key(self.locators.EMAIL_FIELD, email)
        self.send_key(self.locators.PASSWORD_FIELD, password)
        self.send_key(self.locators.REPASSWORD_FIELD, repassword)
        if agree:
            self.click_elem(self.locators.ACCEPT_CHEKBOX)
        self.click_elem(self.locators.SUBMIT_BUTTON)
        if self.driver.current_url == self.url:
            return RegistrationPage(driver=self.driver)
        elif self.driver.current_url.find(MainPage.url) !=-1:
            return MainPage(driver=self.driver)

    def go_to_login(self):
        self.click_elem(self.locators.LOGIN_BUTTON)
        from pages.login_page import LoginPage
        return LoginPage(driver=self.driver)
        
    @property
    def error_message_text(self):
       return self.check_visibility_of_elem(self.locators.ERROR_MESSAGE).text
