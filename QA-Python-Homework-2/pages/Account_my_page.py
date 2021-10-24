from pages.Base_page import Base_page
from locators.All_locators import AccountMyPageLocators

class Account_my_page(Base_page):

    url = 'https://account.my.com/login'

    locators = AccountMyPageLocators()
    