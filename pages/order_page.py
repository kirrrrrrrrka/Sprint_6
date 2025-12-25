from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_first_page(self, name, surname, address, phone):
        self.find_element(self.locators.NAME_FIELD).send_keys(name)
        self.find_element(self.locators.SURNAME_FIELD).send_keys(surname)
        self.find_element(self.locators.ADDRESS_FIELD).send_keys(address)
        
        self.find_element(self.locators.METRO_FIELD).click()
        self.find_element(self.locators.METRO_STATION).click()
        
        self.find_element(self.locators.PHONE_FIELD).send_keys(phone)
        self.find_element(self.locators.NEXT_BUTTON).click()

    def fill_second_page(self, date, rental_period, color, comment=""):
        date_field = self.find_element(self.locators.DATE_FIELD)
        date_field.clear()
        date_field.send_keys(date)
        
        date_field.send_keys(Keys.ESCAPE)
        
        self.find_element(self.locators.RENTAL_PERIOD_FIELD).click()
        if rental_period == "сутки":
            self.find_element(self.locators.RENTAL_PERIOD_OPTION).click()
        elif rental_period == "двое суток":
            self.find_element(self.locators.RENTAL_PERIOD_TWO_DAYS).click()
        
        if color == "серая безысходность" in color:
            self.find_element(self.locators.COLOR_GREY).click()
        else:
            self.find_element(self.locators.COLOR_BLACK).click()
        
        if comment:
            self.find_element(self.locators.COMMENT_FIELD).send_keys(comment)
        
        self.find_element(self.locators.ORDER_BUTTON).click()
        
    def wait_for_order_page_to_load(self):
        """Ожидание загрузки страницы заказа"""
        self.wait_for_element_to_be_visible(self.locators.NAME_FIELD)

    def wait_for_success_modal(self):
        """Ожидание появления модального окна успеха"""
        self.wait_for_element_to_be_visible(self.locators.SUCCESS_MODAL)

    def wait_for_confirmation_modal_to_disappear(self):
        """Ожидание исчезновения модального окна подтверждения"""
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.locators.CONFIRMATION_MODAL)
        )

    def confirm_order(self):
        self.find_element(self.locators.CONFIRM_YES_BUTTON).click()

    def cancel_order(self):
        self.find_element(self.locators.CONFIRM_NO_BUTTON).click()

    def get_success_message(self):
        return self.find_element(self.locators.SUCCESS_TITLE).text

    def get_order_number(self):
        return self.find_element(self.locators.ORDER_NUMBER).text

    def is_confirmation_modal_displayed(self):
        try:
            return self.find_element(self.locators.CONFIRMATION_MODAL, timeout=5).is_displayed()
        except:
            return False

    def is_success_modal_displayed(self):
        try:
            return self.find_element(self.locators.SUCCESS_MODAL, timeout=5).is_displayed()
        except:
            return False