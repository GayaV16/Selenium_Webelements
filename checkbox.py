import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
options = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
for option in options:
    if(option.get_attribute("value")== "option1"):
        option.click()
        time.sleep(1)
        assert (option.is_selected())
        break
screenshot_path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\Webpage Elements\\screenshots\\checkbox1.png"
driver.save_screenshot(screenshot_path)

#Alternative method
driver1 = webdriver.Chrome()
driver1.get("https://rahulshettyacademy.com/AutomationPractice/")
driver1.find_element(By.XPATH,"//input[@id='checkBoxOption3']").click()
time.sleep(1)
screenshot_path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\Webpage Elements\\screenshots\\checkbox2.png"
driver.save_screenshot(screenshot_path)