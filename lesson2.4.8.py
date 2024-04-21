# Explicit Waits (WebDriverWait и expected_conditions) -явные ожидания (дождаться, когда кнопка станет кликабельной)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button2 = browser.find_element(By.ID, "book")
button2.click()
browser.implicitly_wait(5)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button1 = browser.find_element(By.ID, "solve")
button1.click()


time.sleep(10)
browser.quit()


