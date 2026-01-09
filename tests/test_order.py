import pytest
import allure
from data.order_data import ORDER_TEST_DATA


class TestOrder:
    """Тесты для заказа самоката"""
    
    @allure.feature("Заказ самоката")
    @allure.story("Точки входа")
    @allure.title("Форма заказа открывается при клике на кнопку '{button_position}'")
    @pytest.mark.parametrize("button_position", ["top", "bottom"])
    def test_order_form_opens_by_button(self, main_page, order_page, button_position):
        """Тест открытия формы заказа через разные кнопки"""
        with allure.step(f"Нажимаем кнопку 'Заказать' ({button_position})"):
            main_page.click_order_button(button_position)
        
        with allure.step("Проверяем загрузку страницы оформления заказа"):
            order_page.wait_for_order_page_to_load()
            
        with allure.step("Проверяем, что поле 'Имя' доступно для ввода"):
            name_field = order_page.find_element(order_page.locators.NAME_FIELD)
            assert name_field.is_displayed() and name_field.is_enabled(), \
                f"Форма заказа не загрузилась при использовании кнопки {button_position}"
    
    @allure.feature("Заказ самоката")
    @allure.story("Позитивные сценарии")
    @allure.title("После заполнения формы появляется окно подтверждения (кнопка: {button_position})")
    @pytest.mark.parametrize("button_position, test_data", [
        ("top", ORDER_TEST_DATA[0]),
        ("bottom", ORDER_TEST_DATA[1])
    ])
    def test_confirmation_modal_appears_after_form_filling(self, main_page, order_page, button_position, test_data):
        """Тест появления модального окна подтверждения после заполнения формы"""
        with allure.step(f"Нажимаем кнопку 'Заказать' ({button_position})"):
            main_page.click_order_button(button_position)
        
        with allure.step("Заполняем первую страницу формы"):
            order_page.fill_first_page(
                name=test_data["name"],
                surname=test_data["surname"],
                address=test_data["address"],
                phone=test_data["phone"]
            )
        
        with allure.step("Заполняем вторую страницу формы"):
            order_page.fill_second_page(
                date=test_data["date"],
                rental_period=test_data["rental_period"],
                color=test_data["color"],
                comment=test_data["comment"]
            )
        
        with allure.step("Нажимаем кнопку 'Заказать' на второй странице"):
            order_page.click_element(order_page.locators.ORDER_BUTTON)
        
        with allure.step("Проверяем отображение модального окна подтверждения"):
            assert order_page.is_confirmation_modal_displayed(), \
                f"Модальное окно подтверждения не отображается при использовании кнопки {button_position}"
    
    @allure.feature("Заказ самоката")
    @allure.story("Позитивные сценарии")
    @allure.title("Успешное оформление заказа с подтверждением")
    def test_successful_order_creation(self, main_page, order_page):
        """Тест успешного оформления заказа с подтверждением"""
        test_data = ORDER_TEST_DATA[0]
        
        with allure.step("Нажимаем верхнюю кнопку 'Заказать'"):
            main_page.click_order_button("top")
        
        with allure.step("Заполняем первую страницу формы"):
            order_page.fill_first_page(
                name=test_data["name"],
                surname=test_data["surname"],
                address=test_data["address"],
                phone=test_data["phone"]
            )
        
        with allure.step("Заполняем вторую страницу формы"):
            order_page.fill_second_page(
                date=test_data["date"],
                rental_period=test_data["rental_period"],
                color=test_data["color"],
                comment=test_data["comment"]
            )
        
        with allure.step("Нажимаем кнопку 'Заказать' на второй странице"):
            order_page.click_element(order_page.locators.ORDER_BUTTON)
        
        with allure.step("Подтверждаем заказ в модальном окне"):
            order_page.confirm_order()
        
        with allure.step("Проверяем отображение модального окна успеха"):
            order_page.wait_for_success_modal()
            assert order_page.is_success_modal_displayed(), \
                "Модальное окно успешного оформления заказа не отображается"
    
    @allure.feature("Заказ самоката")
    @allure.story("Позитивные сценарии")
    @allure.title("Генерация номера заказа при успешном оформлении")
    def test_order_number_generation(self, main_page, order_page):
        """Тест генерации номера заказа при успешном оформлении"""
        test_data = ORDER_TEST_DATA[0]
        
        with allure.step("Нажимаем верхнюю кнопку 'Заказать'"):
            main_page.click_order_button("top")
        
        with allure.step("Заполняем первую страницу формы"):
            order_page.fill_first_page(
                name=test_data["name"],
                surname=test_data["surname"],
                address=test_data["address"],
                phone=test_data["phone"]
            )
        
        with allure.step("Заполняем вторую страницу формы"):
            order_page.fill_second_page(
                date=test_data["date"],
                rental_period=test_data["rental_period"],
                color=test_data["color"],
                comment=test_data["comment"]
            )
        
        with allure.step("Нажимаем кнопку 'Заказать' на второй странице"):
            order_page.click_element(order_page.locators.ORDER_BUTTON)
        
        with allure.step("Подтверждаем заказ в модальном окне"):
            order_page.confirm_order()
        
        with allure.step("Ожидаем появления модального окна успеха"):
            order_page.wait_for_success_modal()
        
        with allure.step("Проверяем наличие номера заказа"):
            order_number = order_page.get_order_number()
            assert order_number, "Номер заказа не сгенерирован"
    
    @allure.feature("Заказ самоката")
    @allure.story("Негативные сценарии")
    @allure.title("Возврат на страницу оформления после отмены заказа")
    def test_return_to_order_page_after_cancellation(self, main_page, order_page):
        """Тест возврата на страницу оформления после отмены заказа"""
        test_data = ORDER_TEST_DATA[0]
        
        with allure.step("Нажимаем верхнюю кнопку 'Заказать'"):
            main_page.click_order_button("top")
        
        with allure.step("Заполняем данные для заказа"):
            order_page.fill_first_page(
                name=test_data["name"],
                surname=test_data["surname"],
                address=test_data["address"],
                phone=test_data["phone"]
            )
        
            order_page.fill_second_page(
                date=test_data["date"],
                rental_period=test_data["rental_period"],
                color=test_data["color"],
                comment=test_data["comment"]
            )
        
        with allure.step("Нажимаем кнопку 'Заказать' на второй странице"):
            order_page.click_element(order_page.locators.ORDER_BUTTON)
        
        with allure.step("Отменяем заказ в модальном окне"):
            order_page.cancel_order()
        
        with allure.step("Проверяем, что остались на странице оформления"):
            assert order_page.find_element(order_page.locators.ORDER_BUTTON).is_displayed(), \
                "Не вернулись на страницу оформления после отмены заказа"