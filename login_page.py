from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "login is absent in current url"
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is missing"
        # assert True
        
    def register_new_user(self, email, password1, password2):
        email_field = self.browser.find_element(*BasePageLocators.USER_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*BasePageLocators.USER_PASSWORD1)
        password_field1.send_keys(password1)
        password_field2 = self.browser.find_element(*BasePageLocators.USER_PASSWORD2)
        password_field2.send_keys(password2)
        registration = self.browser.find_element(*BasePageLocators.REGISTER)
        registration.click()
        
        
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
        " probably unauthorised user"