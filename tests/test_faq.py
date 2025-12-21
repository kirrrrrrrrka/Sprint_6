import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait


class TestFAQ:
    
    @allure.title("Проверка раздела 'Вопросы о важном'")
    @allure.description("Проверка раскрытия ответов при клике на вопросы")
    @pytest.mark.parametrize("question_index, expected_answer", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_faq_questions(self, main_page, question_index, expected_answer):
        with allure.step(f"Кликаем на вопрос №{question_index + 1}"):
            main_page.click_faq_question(question_index)
        
        with allure.step("Получаем текст ответа"):
            actual_answer = main_page.get_faq_answer_text(question_index)
        
        with allure.step("Проверяем соответствие текста ответа"):
            assert actual_answer == expected_answer, \
                f"Ожидался ответ: '{expected_answer}', но получен: '{actual_answer}'"
    
    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirect(self, main_page, driver):
        with allure.step("Кликаем на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверяем URL текущей страницы"):
            current_url = driver.current_url
            assert current_url == main_page.base_url, \
                f"Ожидался URL: {main_page.base_url}, но получен: {current_url}"
    
    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, main_page, driver):
        with allure.step("Запоминаем текущее окно"):
            main_window = driver.current_window_handle
    
        with allure.step("Кликаем на логотип Яндекса"):
            main_page.click_yandex_logo()
    
        with allure.step("Ждем открытия нового окна и переключаемся на него"):
        # Ждём появления новой вкладки
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            new_window = [window for window in driver.window_handles if window != main_window][0]
            driver.switch_to.window(new_window)
    
        with allure.step("Ждём загрузки страницы и проверяем URL"):
            # Ждём, пока URL перестанет быть about:blank
            WebDriverWait(driver, 15).until(
                lambda d: d.current_url != "about:blank" and d.current_url != ""
            )
        
        # Даём дополнительное время для возможных редиректов
        import time
        time.sleep(2)
        
        current_url = driver.current_url
        print(f"Текущий URL после перехода: {current_url}")  # Для отладки
        
        # Проверяем, что URL содержит dzen.ru (или yandex.ru для редиректа)
        assert any(domain in current_url for domain in ["dzen.ru", "yandex.ru"]), \
            f"Ожидался переход на dzen.ru или yandex.ru, но получен URL: {current_url}"
    
        with allure.step("Закрываем новое окно и возвращаемся к основному"):
            driver.close()
            driver.switch_to.window(main_window)