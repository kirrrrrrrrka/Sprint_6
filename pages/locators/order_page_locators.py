from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Page 1
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//div[text()='Сокольники']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Page 2
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker__day--020")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    
    # Color checkboxes - исправленные локаторы
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    
    # Confirmation modal
    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    CONFIRM_NO_BUTTON = (By.XPATH, "//button[text()='Нет']")
    
    # Success modal
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_TITLE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    ORDER_NUMBER = (By.CLASS_NAME, "Order_Text__2broi")