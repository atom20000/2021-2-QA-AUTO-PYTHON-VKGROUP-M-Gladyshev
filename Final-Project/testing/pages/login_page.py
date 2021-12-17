from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from locators.all_locators import LoginPageLocators



class LoginPage(BasePage):
    
    locators = LoginPageLocators()

    url = 'http://qa_myapp_proxy:8082/login'

    def login(self, username, password):
        self.send_key(self.locators.USERNAME_FIELD, username)
        self.send_key(self.locators.PASSWORD_FIELD, password)
        self.click_elem(self.locators.SUBMIT_BUTTON)
        if self.driver.current_url == self.url:
            return LoginPage(driver=self.driver)
        elif self.driver.current_url.find(MainPage.url) !=-1:
            return MainPage(driver=self.driver)
        print(self.driver.current_url)
    
    def go_to_registration(self):
        self.click_elem(self.locators.CREATE_USER_BUTTON)
        return RegistrationPage(driver=self.driver)