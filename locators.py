from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRODUCT_NAMEORIGINAL = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    PRODUCT_PRICEORIGINAL = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    VIEW_TO_CART = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CONTINUE_SHOPPING = (By.XPATH, "//*[@id='content_inner']/p/a")
    USER_ICON = (By.CLASS_NAME, "icon-user")
    USER_EMAIL = (By.XPATH, "//*[@id='id_registration-email']")
    USER_PASSWORD1 = (By.XPATH, "//*[@id='id_registration-password1']")
    USER_PASSWORD2 = (By.XPATH, "//*[@id='id_registration-password2']")
    REGISTER = (By.NAME, "registration_submit")
    