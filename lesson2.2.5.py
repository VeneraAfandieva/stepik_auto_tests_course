from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"



browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Venera")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Afandieva")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("venera.af@gmail.com")
    
current_dir = os.path.abspath(os.path.dirname(__file__))    
file_name = "newtxt.txt"
file_path = os.path.join(current_dir, file_name)
input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']")
input4.send_keys(file_path) 
   
    
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
  


    
time.sleep(10)
browser.quit()
    
