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
        with allure.step("Запоминаем текущее окно"):
            main_window = main_page.get_current_window_handle()
    
        with allure.step("Кликаем на логотип Яндекса"):
            main_page.click_yandex_logo()
    
        with allure.step("Ждем открытия нового окна"):
            main_page.wait_for_new_window([main_window])
            
            # Находим новое окно
            new_window = [window for window in main_page.get_window_handles() 
                         if window != main_window][0]
            main_page.switch_to_window(new_window)
    
        with allure.step("Проверяем, что перешли на страницу Дзен или Яндекс"):
            # Даем время для редиректов
            main_page.wait.until(
                lambda driver: "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url
            )
            
            current_url = main_page.get_current_url()
            
            assert any(domain in current_url for domain in ["dzen.ru", "yandex.ru"]), \
                f"Ожидался переход на dzen.ru или yandex.ru, но получен URL: {current_url}"
        
    
        main_page.switch_to_window(main_window)