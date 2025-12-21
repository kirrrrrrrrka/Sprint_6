from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    # Page 1
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//div[text()='Сокольники']")  # Updated to match actual station
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Page 2
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker__day--020")  # Example for 20th day
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "gray")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    
    # Confirmation modal
    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")  # Updated locator
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    CONFIRM_NO_BUTTON = (By.XPATH, "//button[text()='Нет']")
    
    # Success modal
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")  # Updated locator
    SUCCESS_TITLE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")  # Updated locator
    ORDER_NUMBER = (By.CLASS_NAME, "Order_Text__2broi")  # Updated locator

    def fill_first_page(self, name, surname, address, phone):
        self.find_element(self.NAME_FIELD).send_keys(name)
        self.find_element(self.SURNAME_FIELD).send_keys(surname)
        self.find_element(self.ADDRESS_FIELD).send_keys(address)
        
        # Select metro station
        self.find_element(self.METRO_FIELD).click()
        self.find_element(self.METRO_STATION).click()
        
        self.find_element(self.PHONE_FIELD).send_keys(phone)
        self.find_element(self.NEXT_BUTTON).click()

    def fill_second_page(self, date, rental_period, color, comment=""):
    # Set date
        self.find_element(self.DATE_FIELD).send_keys(date)
    # Закрыть календарь
        from selenium.webdriver.common.keys import Keys
        self.find_element(self.DATE_FIELD).send_keys(Keys.ESCAPE)
    
    # Select rental period
        self.find_element(self.RENTAL_PERIOD_FIELD).click()
        if rental_period == "сутки":
            self.find_element(self.RENTAL_PERIOD_OPTION).click()
        elif rental_period == "двое суток":
            self.find_element(self.RENTAL_PERIOD_TWO_DAYS).click()
        
        # Select color
        if color == "black":
            self.find_element(self.COLOR_BLACK).click()
        elif color == "grey":
            self.find_element(self.COLOR_GREY).click()
        
        # Add comment if provided
        if comment:
            self.find_element(self.COMMENT_FIELD).send_keys(comment)
        
        self.find_element(self.ORDER_BUTTON).click()

    def confirm_order(self):
        self.find_element(self.CONFIRM_YES_BUTTON).click()

    def cancel_order(self):
        self.find_element(self.CONFIRM_NO_BUTTON).click()

    def get_success_message(self):
        return self.find_element(self.SUCCESS_TITLE).text

    def get_order_number(self):
        return self.find_element(self.ORDER_NUMBER).text

    def is_confirmation_modal_displayed(self):
        return self.find_element(self.CONFIRMATION_MODAL).is_displayed()

    def is_success_modal_displayed(self):
        return self.find_element(self.SUCCESS_MODAL).is_displayed()