from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_first_page(self, name, surname, address, phone, metro_station="Сокольники"):
        self.find_element(self.locators.NAME_FIELD).send_keys(name)
        self.find_element(self.locators.SURNAME_FIELD).send_keys(surname)
        self.find_element(self.locators.ADDRESS_FIELD).send_keys(address)
        
        # Выбор станции метро (используем переданный параметр или значение по умолчанию)
        self.select_metro_station(metro_station)
        
        self.find_element(self.locators.PHONE_FIELD).send_keys(phone)
        self.find_element(self.locators.NEXT_BUTTON).click()

    def select_metro_station(self, station_name):
        """Выбор станции метро"""
        self.find_element(self.locators.METRO_FIELD).click()
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.find_element(station_locator).click()

    def fill_second_page(self, date, rental_period, color, comment=""):
        # Заполнение даты
        self.set_delivery_date(date)
        
        # Выбор срока аренды
        self.select_rental_period(rental_period)
        
        # Выбор цвета
        self.select_color(color)
        
        # Заполнение комментария
        if comment:
            self.find_element(self.locators.COMMENT_FIELD).send_keys(comment)

    def set_delivery_date(self, date):
        """Установка даты доставки"""
        date_field = self.find_element(self.locators.DATE_FIELD)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ESCAPE)

    def select_rental_period(self, period):
        """Выбор срока аренды"""
        self.find_element(self.locators.RENTAL_PERIOD_FIELD).click()
        period_locator = (By.XPATH, f"//div[text()='{period}']")
        self.find_element(period_locator).click()

    def select_color(self, color):
        """Выбор цвета самоката"""
        if color == "grey":
            self.find_element(self.locators.COLOR_GREY_CHECKBOX).click()
        elif color == "black":
            self.find_element(self.locators.COLOR_BLACK_CHECKBOX).click()

    def wait_for_order_page_to_load(self):
        """Ожидание загрузки страницы заказа"""
        self.wait_for_element_to_be_visible(self.locators.NAME_FIELD)

    def wait_for_success_modal(self):
        """Ожидание появления модального окна успеха"""
        self.wait_for_element_to_be_visible(self.locators.SUCCESS_MODAL)
    
    def wait_for_confirmation_modal(self):
        """Ожидание появления модального окна подтверждения"""
        self.wait_for_element_to_be_visible(self.locators.CONFIRMATION_MODAL)

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