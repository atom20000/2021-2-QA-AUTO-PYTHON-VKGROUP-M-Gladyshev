from pages.Main_page import Main_page
from locators.All_locators import DashboardPageLocators
import numpy
from PIL import Image

class Dashboard_page(Main_page):

    locators = DashboardPageLocators()

    
    
    @property
    def Generation_Image(self):
        return Image.fromarray((numpy.random.rand(100,100,3) * 255).astype('uint8')).convert('RGBA')