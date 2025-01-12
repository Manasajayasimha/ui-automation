import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import TestData

@pytest.fixture(scope="session")
def init_driver(request):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(TestData.BASE_URL)
    driver.implicitly_wait(10)
    
    yield driver
    driver.close()