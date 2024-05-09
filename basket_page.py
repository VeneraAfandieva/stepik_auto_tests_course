# импортировать нужное нам исключение
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException 
from .locators import BasePageLocators

class BasketPage():
## проверка, что в корзине нет товаров и есть сообщение о пустой корзине  
    def art_should_be_empty(self):
        assert self.is_element_present(*BasePageLocators.CONTINUE_SHOPPING)
    
    