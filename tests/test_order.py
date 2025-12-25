import pytest
import allure



class TestOrder:
    
    @allure.title("Оформление заказа через верхнюю кнопку")
    @allure.description("Проверка полного флоу оформления заказа")
    @pytest.mark.parametrize("order_button_position, test_data", [
        ("top", {
            "name": "Вася",
            "surname": "Пупкин",
            "address": "Москва, ул. Автозаводская 13",
            "phone": "79997977574",
            "date": "20.12.2025",
            "rental_period": "сутки",
            "color": "серая безысходность",
            "comment": "Позвоните за час"
        }),
        ("bottom", {
            "name": "Марина",
            "surname": "Пупкина",
            "address": "Москва, ул. Маршала Василевского 15",
            "phone": "79669696996",
            "date": "21.12.2025",
            "rental_period": "двое суток",
            "color": "серая безысходность",
            "comment": "Оставьте у подъезда"
        })
    ])
    def test_order_creation(self, main_page, order_page, driver, order_button_position, test_data):
        with allure.step(f"Нажимаем кнопку 'Заказать' ({order_button_position})"):
            if order_button_position == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()
        
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
        
        with allure.step("Проверяем отображение модального окна подтверждения"):
            assert order_page.is_confirmation_modal_displayed(), \
                "Модальное окно подтверждения не отображается"
        
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверяем отображение модального окна успеха"):
            order_page.wait_for_success_modal()
            assert order_page.is_success_modal_displayed(), \
                "Модальное окно успешного оформления заказа не отображается"
        
        with allure.step("Проверяем сообщение об успешном оформлении заказа"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Ожидалось сообщение 'Заказ оформлен', но получено: {success_message}"
        
        with allure.step("Проверяем наличие номера заказа"):
            order_number = order_page.get_order_number()
            assert order_number, "Номер заказа не сгенерирован"
            
            allure.attach(
                f"Номер заказа: {order_number}",
                name="Номер заказа",
                attachment_type=allure.attachment_type.TEXT
            )
    
    @allure.title("Отмена заказа в модальном окне подтверждения")
    def test_order_cancellation(self, main_page, order_page, driver):
        with allure.step("Нажимаем верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        
        with allure.step("Заполняем минимальные данные для первой страницы"):
            order_page.fill_first_page(
                name="Тест",
                surname="Тестов",
                address="Москва, тестовая улица",
                phone="79999999999"
            )
        
        with allure.step("Заполняем минимальные данные для второй страницы"):
            order_page.fill_second_page(
                date="20.12.2025",
                rental_period="сутки",
                color="серая безысходность"
            )
        
        with allure.step("Проверяем отображение модального окна подтверждения"):
            assert order_page.is_confirmation_modal_displayed(), \
                "Модальное окно подтверждения не отображается"
        
        with allure.step("Отменяем заказ"):
            order_page.cancel_order()
        
        with allure.step("Проверяем, что остались на странице оформления"):
            order_page.wait_for_confirmation_modal_to_disappear()
            assert order_page.find_element(order_page.locators.ORDER_BUTTON).is_displayed(), \
                "Не вернулись на страницу оформления после отмены"