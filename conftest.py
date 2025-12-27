import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="function")
def driver():
   
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    try:
        driver = webdriver.Firefox(options=options)
    except Exception as e:
        print(f"Ошибка при создании драйвера: {e}")
        print("Попробуем альтернативный способ...")

        service = Service("/usr/local/bin/geckodriver")
        driver = webdriver.Firefox(service=service, options=options)
    
    driver.maximize_window()
    
    yield driver
    
    # Закрываем все окна кроме основного
    if len(driver.window_handles) > 1:
        main_window = driver.window_handles[0]
        for handle in driver.window_handles[1:]:
            driver.switch_to.window(handle)
            driver.close()
        driver.switch_to.window(main_window)
    
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