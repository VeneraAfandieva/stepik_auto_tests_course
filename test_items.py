from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
    
        # Открываем страницу товара
        browser.get(link)
        
        # Установлено время принудительной задержки браузера
        time.sleep(30)
        
        # Проверяем наличие кнопки добавления товара в корзину
        message = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        assert "Ajouter au panier" in message.text