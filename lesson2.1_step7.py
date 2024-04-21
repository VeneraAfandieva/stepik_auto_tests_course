from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

#открываю страницу
link = "http://suninjuly.github.io/get_attribute.html"
#считаем математическую функцию
def formula(x):
   #определение значения, которое функция возвращает при вызове
   return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()
browser.get(link)

##Нашла сундук
sunduk_kartinka = browser.find_element(By.ID, "treasure")
#значение х
znachenie_x=sunduk_kartinka.get_attribute("valuex")
print(znachenie_x)
y = formula(znachenie_x)
# print(y)


#нашла поле ввода
input = browser.find_element(By.ID, "answer")
#ввод в поле рез-та
input.send_keys(y)


option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option4 = browser.find_element(By.ID, "robotsRule")
option4.click()
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()


time.sleep(10)
browser.quit()