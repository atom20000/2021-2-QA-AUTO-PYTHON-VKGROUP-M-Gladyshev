from locators.All_locators import *
from Base_class import BaseCase
import pytest

class TestClass(BaseCase):

#Тест по проверке входа

    #@pytest.mark.skip("SKIP")
    @pytest.mark.UI
    def test_login(self,login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'


#Тест по проверке выхода

    #@pytest.mark.skip("SKIP")
    @pytest.mark.UI
    def test_logout(self,login):
        self.logout()
        assert self.driver.current_url == 'https://target.my.com/'


#Тест по проверке изменения контактной информации

    #@pytest.mark.skip("SKIP")
    @pytest.mark.UI
    def test_contact(self,login,set_contact_inf):
        self.check_button_not_hidden(Main_page.PROFILE_BUTTON, Main_page.OTHER_CENTRAL_BUTTON)
        self.send_key(Contact_Form.FIO_FIELD,set_contact_inf[0])
        self.send_key(Contact_Form.PHONE_FIELD,set_contact_inf[1])
        self.click_elem(Contact_Form.BUTTON_SAVE_CHANGE)
        self.driver.refresh()
        assert (self.find_elem(Contact_Form.FIO_FIELD).get_attribute('value') == set_contact_inf[0] 
        and self.find_elem(Contact_Form.PHONE_FIELD).get_attribute('value') == set_contact_inf[1])
        self.logout()
    

#Тест по проверке перехода на вкладки Аудитория и Инструменты    

    #@pytest.mark.skip("SKIP")
    @pytest.mark.UI
    @pytest.mark.parametrize(
        'locator, url',
        [
            (Main_page.AUDITORIUM_BUTTON,'https://target.my.com/segments'),
            (Main_page.TOOLS_BUTTON,'https://target.my.com/tools')
        ]
    )
    def test_central_buttons(self, login, locator, url):
        self.check_button_not_hidden(locator, Main_page.OTHER_CENTRAL_BUTTON)
        assert self.driver.current_url.find(url) !=-1
        self.logout()
