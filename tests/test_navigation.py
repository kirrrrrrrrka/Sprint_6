import pytest
import allure


class TestNavigation:
    """Тесты навигации по сайту"""
    
    @allure.feature("Навигация")
    @allure.story("Переход по логотипам")
    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirect(self, main_page):
        with allure.step("Кликаем на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверяем, что перешли на главную страницу"):
            current_url = main_page.get_current_url()
            expected_url = main_page.base_url
            
            assert current_url == expected_url, \
                f"Ожидался переход на главную страницу: {expected_url}, но текущий URL: {current_url}"
    
    @allure.feature("Навигация")
    @allure.story("Переход по логотипам")
    @allure.title("Проверка перехода на Яндекс.Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect_to_dzen(self, main_page):
        with allure.step("Проверяем редирект на Яндекс.Дзен"):
            redirected_url = main_page.check_yandex_redirect_to_dzen()
            
            #проверяем домен Дзен
            assert "dzen.ru" in redirected_url, \
                f"Ожидался переход на Яндекс.Дзен (dzen.ru), но получен URL: {redirected_url}"