from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/redirect_accept.html"


browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CLASS_NAME, "trollface")
button.click()
time.sleep(1)

link2 = "https://suninjuly.github.io/redirect_page.html?"

browser.get(link2)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
print(x_element.text)
x = x_element.text

y = calc(x)


# # # # y_element= browser.find_element(By.ID, "answer")
# # # # y=y_element.text
input = browser.find_element(By.CLASS_NAME, "form-control")
print(input)
input.send_keys("фффф")



# # option1 = browser.find_element(By.ID, "robotCheckbox")
# # option1.click()
# # option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
# # option2.click()
# # option3 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
# # option3.click()
# # option4 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
# # option4.click()
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()


time.sleep(10)
browser.quit()
