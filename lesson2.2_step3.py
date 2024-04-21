# работа с выпадающим списком
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

#открыла ссылку
link = "http://suninjuly.github.io/selects1.html"
#посчитала формулу
def calc(x, y):
    return str(int(x) + int(y))


browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "num1")
x=x_element.text
y_element = browser.find_element(By.ID, "num2")
y=y_element.text
#список раскрылся
browser.find_element(By.TAG_NAME, "select").click()

z = calc(x, y)
print(z)

browser.find_element(By.CSS_SELECTOR, "[value='" + z + "']").click()
print("[value=" + z + "]")

time.sleep(10)

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()


time.sleep(5)
browser.quit()