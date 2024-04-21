from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"


browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

y = calc(x)



input = browser.find_element(By.ID, "answer")
input.send_keys(y)


option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option4 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option4.click()
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()


time.sleep(10)
browser.quit()