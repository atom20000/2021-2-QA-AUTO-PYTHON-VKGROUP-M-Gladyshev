from pages.base_page import BasePage
from locators.all_locators import AccountMyPageLocators

class AccountMyPage(BasePage):

    url = 'https://account.my.com/login'

    locators = AccountMyPageLocators()
    