from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators.main_page_locators import MainPageLocators
from data.faq_data import FAQ_DATA
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def get_faq_questions(self):
        return self.find_elements(self.locators.FAQ_QUESTIONS)

    def get_faq_answers(self):
        return self.find_elements(self.locators.FAQ_ANSWERS)

    def click_faq_question(self, index):
        questions = self.get_faq_questions()
        question = questions[index]
        
        answer = self.get_faq_answers()[index]
        is_expanded_before = answer.is_displayed()
        
        self.execute_script("arguments[0].click();", question)
        
        if not is_expanded_before:
            self.wait.until(
                lambda driver: self.get_faq_answers()[index].is_displayed()
            )
        else:
            self.wait.until(
                lambda driver: not self.get_faq_answers()[index].is_displayed()
            )
        
        return question

    def get_faq_answer_text(self, index):
        answers = self.get_faq_answers()
        self.wait.until(
            lambda driver: answers[index].is_displayed() and answers[index].text.strip() != ""
        )
        return answers[index].text

    def get_faq_question_text(self, index):
        questions = self.get_faq_questions()
        return questions[index].text

    def click_order_button_top(self):
        top_buttons = self.find_elements(self.locators.ORDER_BUTTON_TOP)
        for button in top_buttons:
            if "Заказать" in button.text:
                button.click()
                return
        top_buttons[0].click()

    def click_order_button_bottom(self):
        bottom_button = self.find_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.execute_script("arguments[0].click();", bottom_button)

    def click_order_button(self, position):
        """Клик по кнопке заказа в указанной позиции"""
        if position == "top":
            self.click_order_button_top()
        elif position == "bottom":
            self.click_order_button_bottom()
        else:
            raise ValueError(f"Неизвестная позиция кнопки: {position}")

    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)

    def is_main_page(self):
        """Проверка, что мы на главной странице"""
        current_url = self.get_current_url()
        return current_url == self.base_url

    def get_expected_faq_answer(self, question_index):
        """Получить ожидаемый текст ответа из данных"""
        return FAQ_DATA[question_index]["answer"]
    
    def get_faq_question_count(self):
        """Получить количество вопросов"""
        return len(self.get_faq_questions())
    
    def wait_for_faq_section(self):
        """Ожидание загрузки секции FAQ"""
        self.wait_for_element_to_be_visible(self.locators.FAQ_SECTION)
    
    def check_yandex_redirect_to_dzen(self):
        """Проверка редиректа на Яндекс.Дзен (https://dzen.ru/)"""
        with allure.step("Запоминаем текущее окно"):
            main_window = self.get_current_window_handle()
        
        with allure.step("Кликаем на логотип Яндекса"):
            self.click_element(self.locators.YANDEX_LOGO)
        
        with allure.step("Ждем открытия нового окна"):
            self.wait_for_new_window([main_window])
            
            new_window = [window for window in self.get_window_handles() 
                         if window != main_window][0]
            self.switch_to_window(new_window)
        
        with allure.step("Ожидаем редирект на Яндекс.Дзен"):
            self.wait_for_url_contains("dzen.ru")
            
            current_url = self.get_current_url()
            
        with allure.step("Возвращаемся в основное окно"):
            self.switch_to_window(main_window)
        
        return current_url
    
    def wait_for_element_to_have_text(self, element, text, timeout=10):
        """Ожидание, что элемент содержит определенный текст"""
        self.wait.until(
            lambda driver: text in element.text
        )