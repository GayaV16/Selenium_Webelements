import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
option = Select(driver.find_element(By.ID,"dropdown-class-example"))
option.select_by_visible_text("Option1")
time.sleep(2)
option.select_by_index(2)
time.sleep(1)
option.select_by_value("option3")
screenshot_path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\Webpage Elements\\screenshots\\dropdown.png"
driver.save_screenshot(screenshot_path)