from Static_var import *
from base import Basecase
import pytest
import re

class TestOne(Basecase):

    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_Command_Russia(self):
        page = self.main_page.Open_Keyboard()
        while len(page.driver.find_elements(*page.locators.BLOCK_OF_RUSSIA)) == 0:
            page.Send_text('Russia')
            try:
                page.find_elem(page.locators.BLOCK_OF_RUSSIA, 3)
            except:
                pass
        page.scroll_by_element(method=page.scroll_element_left,locator_elem=page.locators.BUTTON_POPULATION_RUSSIAN, locator=page.locators.CAROUSEL_FACT, right_x=int(page.driver.get_window_size()['width'])*0.25)
        page.click_elem(page.locators.BUTTON_POPULATION_RUSSIAN)
        assert page.find_elem(page.locators.RESPONSE_POPULATION_RUSSIAN).get_attribute('text').find('146 млн') !=-1

    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_Command_Calculator(self):
        page = self.main_page.Open_Keyboard()
        page.Send_text('40+5*2')
        assert page.find_elem((page.locators.RESPONSE_CALCULATE[0],page.locators.RESPONSE_CALCULATE[1].format(f'{40+5*2}'))).get_attribute('text') == str(40+5*2)
    
    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_source_news(self):
        page = self.main_page.Open_Settings()
        page = page.Go_to_Source_News()
        page.click_elem(page.locators.BUTTON_CHOICE_VESTE_FM)
        assert page.find_elem(page.locators.CONFIRM_CHOICE)
        page = page.Retun_Settings()
        page = page.Exit_Settings()
        page = page.Open_Keyboard()
        page.Send_text('News')
        assert re.match(r'Вести (ФМ|FM)', page.find_elem(page.locators.PLAYER_TRACK_NAME).get_attribute('text'))
    
    #@pytest.mark.skip('SKIP')
    @pytest.mark.Android
    def test_about_app(self):
        page = self.main_page.Open_Settings()
        page = page.Go_to_About()
        app_name = os.path.basename(CAPABILITY['app'])
        assert page.find_elem(page.locators.VERSION_APP).get_attribute('text').find(app_name[app_name.rfind('v')+1:app_name.rfind('.')])
        assert page.find_elem(page.locators.COPYRIGHT_APP).get_attribute('text').lower().find('все права защищены') != -1

