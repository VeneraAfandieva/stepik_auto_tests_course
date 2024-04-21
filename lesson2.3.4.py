# принимаем alert
# Alert является модальным окном: это означает, что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert. 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"



browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CLASS_NAME, "btn")
input1.click()
confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

y  = calc(x)

input2 = browser.find_element(By.ID, "answer")
input2.send_keys(y)

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
  


    
time.sleep(10)
browser.quit()
    
