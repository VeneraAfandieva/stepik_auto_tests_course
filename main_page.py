# импорт базового класса BasePage:
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


# создаем класс  MainPage:
class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
         
    # модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented" -с данным селектором будет выходить ошибка

# class MainPage(BasePage):
#     def __init__(self, *args, **kwargs):
#         super(MainPage, self).__init__(*args, **kwargs)
        
 