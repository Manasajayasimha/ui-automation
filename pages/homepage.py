from config.config import TestData
from pages.basepage import Basepage
import locators

class Homepage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)
    
    def is_search_box_visible(self):
        return self.is_visible(locators.SEARCH)
    
    def send_search_text(self,text):
        return self.send_text(locators.SEARCH,text)
    
    def get_product_list(self):
        return self.get_list(locators.PRODUCT_LIST)