import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    
    driver = webdriver.Firefox(options=options)
    
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    page = MainPage(driver)
    page.go_to_site()
    return page


@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    page = OrderPage(driver)
    return page