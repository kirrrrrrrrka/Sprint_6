import pytest
import allure
from data.faq_data import FAQ_DATA


class TestFAQ:
    
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
    
    @allure.feature("Навигация")
    @allure.story("Переход по логотипам")
    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirect(self, main_page):
        with allure.step("Кликаем на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверяем, что перешли на главную страницу"):
            assert main_page.is_main_page(), \
                f"Ожидался переход на главную страницу: {main_page.base_url}"
    
    @allure.feature("Навигация")
    @allure.story("Переход по логотипам")
    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, main_page):
        with allure.step("Проверяем редирект на Яндекс/Дзен"):
            redirected_url = main_page.check_yandex_redirect()
            
            assert any(domain in redirected_url for domain in ["dzen.ru", "yandex.ru"]), \
                f"Ожидался переход на dzen.ru или yandex.ru, но получен URL: {redirected_url}"