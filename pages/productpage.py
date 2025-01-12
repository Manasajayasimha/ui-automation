
from pages.basepage import Basepage
import locators

class ProductPage(Basepage):
    
    def __init__(self,driver):
        super().__init__(driver)
        
    def get_product_title(self):
        return self.get_title(locators.PRODUCT_TITLE)
    
    def add_to_cart(self):
        return self.click(locators.ADD_TO_CART)
        
    def get_cart_size(self):
        return self.get_value(locators.CART_VALUE)