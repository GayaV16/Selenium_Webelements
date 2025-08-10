import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"autocomplete").send_keys("Germany")
countries = driver.find_elements(By.XPATH,'//li[@class="ui-menu-item"]/div')
print(len(countries))
for country in countries:
    if(country.text == "Germany"):
        country.click()
        break
time.sleep(2)
value = driver.find_element(By.ID,"autocomplete").get_attribute("value")
print(value)
assert (value == "Germany")
time.sleep(2)
screenshot_path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\Webpage Elements\\screenshots\\searchbox.png"
driver.save_screenshot(screenshot_path)
