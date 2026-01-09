import pytest
import allure
from data.faq_data import FAQ_DATA


class TestFAQ:
    """Тесты для раздела 'Вопросы о важном'"""
    
    @allure.feature("FAQ")
    @allure.story("Работа с вопросами о важном")
    @allure.title("Проверка раздела 'Вопросы о важном'")
    @allure.description("Проверка раскрытия ответов при клике на вопросы")
    @pytest.mark.parametrize("question_index", list(range(len(FAQ_DATA))))
    def test_faq_questions(self, main_page, question_index):
        expected_answer = FAQ_DATA[question_index]["answer"]
        
        with allure.step(f"Кликаем на вопрос №{question_index + 1}"):
            main_page.click_faq_question(question_index)
        
        with allure.step("Получаем текст ответа"):
            actual_answer = main_page.get_faq_answer_text(question_index)
        
        with allure.step("Проверяем соответствие текста ответа"):
            assert actual_answer == expected_answer, \
                f"Ожидался ответ: '{expected_answer}', но получен: '{actual_answer}'"