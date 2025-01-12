from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Basepage:
    def __init__(self,driver):
        self.driver=driver

    def click(self,locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,locator))).click()

    def _send_keys(self,locator, text):
        wdw = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,locator)))
        wdw.send_keys(text)
        wdw.submit()
    
    def send_text(self,locator,text):
        self.click(locator)
        self._send_keys(locator, text)
    
    def _locate(self, locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,locator)))
        
    def is_visible(self,locator):
        res=self._locate(locator)
        return bool(res)
    
    def get_title(self, locator):
        res=self._locate(locator)
        return res.text

    def get_value(self, locator):
        res=self._locate(locator)
        return int(res.text)
    
    def get_list(self,locator):
        item_list=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,locator)))
        return item_list
    
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    