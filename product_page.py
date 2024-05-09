# импортировать нужное нам исключение
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        PRODUCT_NAME = self.browser.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1").text
        PRODUCT_NAMEORIGINAL = self.browser.find_element(By.XPATH, "//*[@id='messages']/div[1]/div/strong").text
        PRODUCT_PRICE = self.browser.find_element(By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]").text
        PRODUCT_PRICEORIGINAL = self.browser.find_element(By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong").text
        assert PRODUCT_NAME == PRODUCT_NAMEORIGINAL and PRODUCT_PRICE == PRODUCT_PRICEORIGINAL, 'Some bug'
        
            
    def view_to_cart(self):
        view_cart = self.browser.find_element(*ProductPageLocators.VIEW_TO_CART)
        view_cart.click()
          
    
    def should_be_product_page(self):
        self.should_be_message_about_adding()
        self.should_be_message_basket_total()
        
        
    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAMEORIGINAL), "Product original name is not presented"
        
    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICEORIGINAL), "Product original name is not presented"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
         "Success message is presented, but should not be"
         
    