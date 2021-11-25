from Static_var import *
from base import Basecase
import pytest
import re

class TestOne(Basecase):

    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_Command_Russia(self):
        page = self.main_page.open_keyboard()
        page.wait_answer_from_command(page.locators.BLOCK_OF_RUSSIA,'Russia',3)
        page.scroll_by_element(method=page.scroll_element_left,locator_elem=page.locators.BUTTON_POPULATION_RUSSIAN, locator=page.locators.CAROUSEL_FACT, right_x=int(page.driver.get_window_size()['width'])*0.25)
        page.click_elem(page.locators.BUTTON_POPULATION_RUSSIAN)
        assert page.get_text_from_element(page.locators.RESPONSE_POPULATION_RUSSIAN).find('146 млн') !=-1

    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_Command_Calculator(self):
        page = self.main_page.open_keyboard()
        page.send_text('40+5*2')
        assert page.get_text_from_element((page.locators.RESPONSE_CALCULATE[0],page.locators.RESPONSE_CALCULATE[1].format(f'{40+5*2}'))) == str(40+5*2)
    
    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_source_news(self):
        page = self.main_page.open_settings()
        page = page.go_to_source_news()
        page.click_elem(page.locators.BUTTON_CHOICE_VESTE_FM)
        assert page.find_elem(page.locators.CONFIRM_CHOICE)
        page = page.retun_settings()
        page = page.exit_settings()
        page = page.open_keyboard()
        page.send_text('News')
        assert re.match(r'Вести (ФМ|FM)', page.get_text_from_element(page.locators.PLAYER_TRACK_NAME))
    
    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_about_app(self):
        page = self.main_page.open_settings()
        page = page.go_to_about()
        app_name = os.path.basename(CAPABILITY['app'])
        assert page.get_text_from_element(page.locators.VERSION_APP).find(app_name[app_name.rfind('v')+1:app_name.rfind('.')])
        assert page.get_text_from_element(page.locators.COPYRIGHT_APP).lower().find('все права защищены') != -1

