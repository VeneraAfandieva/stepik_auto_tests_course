
# при появлении тестируемого элемента с задержкой, можно добавить time.sleep, но это не эффективно.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")

# time.sleep(1)
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text

# time.sleep(10)

# при появлении тестируемого элемента с задержкой, используется метод - Selenium Waits (Implicit Waits) -неявным ожидание

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")


button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

time.sleep(10)