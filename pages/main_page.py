from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators.main_page_locators import MainPageLocators
from data.faq_data import FAQ_DATA


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
        
        # Ожидаем изменения состояния ответа
        if not is_expanded_before:
            # Если был свернут, ждем пока станет видимым
            self.wait.until(
                lambda driver: self.get_faq_answers()[index].is_displayed()
            )
        else:
            # Если был развернут, ждем пока скроется
            self.wait.until(
                lambda driver: not self.get_faq_answers()[index].is_displayed()
            )
        
        return question

    def get_faq_answer_text(self, index):
        answers = self.get_faq_answers()
        # Ждем, чтобы ответ был видимым перед получением текста
        self.wait.until(
            lambda driver: answers[index].is_displayed() and answers[index].text.strip() != ""
        )
        return answers[index].text

    def get_faq_question_text(self, index):
        questions = self.get_faq_questions()
        return questions[index].text

    def click_order_button_top(self):
        top_buttons = self.find_elements(self.locators.ORDER_BUTTON_TOP)
    
    # Ищем кнопку с текстом "Заказать"
        for button in top_buttons:
            if "Заказать" in button.text:
                button.click()
                return
    
        top_buttons[0].click()

    def click_order_button_bottom(self):
        bottom_button = self.find_element(self.locators.ORDER_BUTTON_BOTTOM)
        
        self.execute_script("arguments[0].click();", bottom_button)

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

    def check_yandex_redirect(self):
        """Проверка редиректа на Яндекс/Дзен после клика по логотипу"""
        # Запоминаем текущее окно
        main_window = self.get_current_window_handle()
    
        # Кликаем на логотип Яндекса
        self.click_element(self.locators.YANDEX_LOGO)
    
        # Ждем открытия нового окна
        self.wait_for_new_window([main_window])
        
        # Находим новое окно
        new_window = [window for window in self.get_window_handles() 
                     if window != main_window][0]
        self.switch_to_window(new_window)
    
        # Ожидаем редирект на Дзен или Яндекс
        self.wait_for_url_matches_pattern(["dzen.ru", "yandex.ru"])
        
        # Получаем текущий URL
        current_url = self.get_current_url()
        
        # Возвращаемся в основное окно
        self.switch_to_window(main_window)
        
        return current_url