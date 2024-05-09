# импортировать нужное нам исключение
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException 
from .locators import BasePageLocators
import time
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
    # команду для неявного ожидания со значением по умолчанию в 10:    
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        time.sleep(5)
    # метод, в котором будем перехватывать исключение    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
  
## проверка, что в корзине нет товаров и есть сообщение о пустой корзине  
    def art_should_be_empty(self):
        assert self.is_element_present(*BasePageLocators.CONTINUE_SHOPPING)
        
#проверку того, что пользователь залогинен 
# def should_be_authorized_user(self):
#     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
#         " probably unauthorised user"
    