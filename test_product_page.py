from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time
# # Задание: независимость контента, ищем баг
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f"{link}"

#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(10)
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.view_to_cart()
#     page.should_be_message_about_adding()
#     page.should_be_message_basket_total()
    
# # Проверяем, что нет сообщения об успехе с помощью is_not_element_present        
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(10)
#     page.add_product_to_basket()
#     page.should_not_be_success_message()
    
# #Проверяем, что нет сообщения об успехе с помощью is_not_element_present 
# marks=pytest.mark.xfail
# def test_guest_cant_see_success_messag(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(10)
#     page.should_not_be_success_message()
      
# # Проверяем, что нет сообщения об успехе с помощью is_disappeared
# def test_message_disappeared_after_adding_product_to_basket(browser):
#      link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#      page = ProductPage(browser, link)
#      page.open()
#      time.sleep(10)
#      page.add_product_to_basket()
#      page.should_not_be_success_message()
     
# ## проверка, что пользователь "видит" кнопку логина на странице продукта  
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
    
#  # проверка, что пользователь может перейти на страницу логина со страницы продукта    
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
    
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.view_to_cart()
#     page.art_should_be_empty()
    
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.view_to_cart()
#     page.art_should_be_empty()
    
    
  
# class TestUserAddToBasketFromProductPage():
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, browser):
#         login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
#         login_page.open()
#         # Генерируем почту, прописываем надежный пароль и регистрируем нового пользователя
#         email = str(time.time()) + "@fakemail.org"
#         password1 = password2 = "Stepik132456"
#         # Регистрируем нового пользователя. Он должен автомтически авторизоваться
#         login_page.register_new_user(email, password1, password2)
#         # Проверяем, что пользователь авторизован
#         login_page.should_be_authorized_user()
        
#     def test_user_can_add_product_to_basket(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()
#         time.sleep(10)
#         page.add_product_to_basket()
#         time.sleep(10)
#         page.should_be_message_about_adding()
#         page.should_be_message_basket_total()
           
#     def test_user_cant_see_success_messag(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()
#         time.sleep(10)
#         page.should_not_be_success_message()
        
        
        
        
        
        
@pytest.mark.need_review       
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        login_page.open()
        # Генерируем почту, прописываем надежный пароль и регистрируем нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password1 = password2 = "Stepik132456"
        # Регистрируем нового пользователя. Он должен автомтически авторизоваться
        login_page.register_new_user(email, password1, password2)
        # Проверяем, что пользователь авторизован
        login_page.should_be_authorized_user()
        
        
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

    page = ProductPage(browser, link)
    page.open()
    time.sleep(10)
    page.add_product_to_basket()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
        
@pytest.mark.need_review   
def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.view_to_cart()
    page.art_should_be_empty()
        
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
        
        
    
    
    
    
    