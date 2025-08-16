import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"openwindow").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print("New window:", driver.title)
driver.switch_to.window(windowsOpened[0])
print("Old window:", driver.title)
