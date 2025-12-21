from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # FAQ section
    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")  # Updated locator
    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion__button")  # Updated locator
    FAQ_ANSWERS = (By.CLASS_NAME, "accordion__panel")  # Updated locator
    
    # FAQ questions texts
    FAQ_QUESTION_1 = "Сколько это стоит? И как оплатить?"
    FAQ_QUESTION_2 = "Хочу сразу несколько самокатов! Так можно?"
    FAQ_QUESTION_3 = "Как рассчитывается время аренды?"
    FAQ_QUESTION_4 = "Можно ли заказать самокат прямо на сегодня?"
    FAQ_QUESTION_5 = "Можно ли продлить заказ или вернуть самокат раньше?"
    FAQ_QUESTION_6 = "Вы привозите зарядку вместе с самокатом?"
    FAQ_QUESTION_7 = "Можно ли отменить заказ?"
    FAQ_QUESTION_8 = "Я живу за МКАДом, привезёте?"
    
    # Order buttons
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")  # First order button
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button")  # Bottom order button
    
    # Logo
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Updated locator
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")  # Updated locator

    def get_faq_questions(self):
        return self.find_elements(self.FAQ_QUESTIONS)

    def get_faq_answers(self):
        return self.find_elements(self.FAQ_ANSWERS)

    def click_faq_question(self, index):
        questions = self.get_faq_questions()
        question = questions[index]
        self.driver.execute_script("arguments[0].click();", question)
        import time
        time.sleep(0.3)
        return question

    def get_faq_answer_text(self, index):
        answers = self.get_faq_answers()
        return answers[index].text

    def click_order_button_top(self):
        order_buttons = self.find_elements(self.ORDER_BUTTON_TOP)
        order_buttons[0].click()

    def click_order_button_bottom(self):
        self.scroll_to_element(self.find_element(self.ORDER_BUTTON_BOTTOM))
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        logo = self.find_element(self.SCOOTER_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)

    def click_yandex_logo(self):
        logo = self.find_element(self.YANDEX_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)