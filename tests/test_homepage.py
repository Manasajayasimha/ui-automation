import pytest
from pages.homepage import Homepage
from pages.productpage import ProductPage
from tests.test_base import BaseTest


class Test_Homepage(BaseTest):
    def test_search_product(self, init_driver):
        homepage=Homepage(init_driver)
        flag=homepage.is_search_box_visible()
        assert flag
        
        SEARCH_TEXT="book"
        homepage.send_search_text(SEARCH_TEXT)
        
        search_items = homepage.get_product_list()
        assert len(search_items) > 0
        
        switchitem = {}
        for item in search_items:
            if item.text:
                item.click()
                switchitem = item.text
                break
        homepage.switch_window()
        product = ProductPage(init_driver)
        assert switchitem == product.get_product_title()
        
    def test_add_cart(self, init_driver):
        product = ProductPage(init_driver)
        product.add_to_cart()
        assert 1 == product.get_cart_size()