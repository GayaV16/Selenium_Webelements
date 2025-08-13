import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,'//a[@id="opentab"]').click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print("Switched to tab with title:", driver.title)
driver.switch_to.window(windowsOpened[0])
print("Switched to tab with title:", driver.title)
time.sleep(1)