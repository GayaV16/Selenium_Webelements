import selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#To accept alert
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Practice")
driver.find_element(By.ID,"alertbtn").click()
alerts = driver.switch_to.alert
print(alerts.text)
alerts.accept()

#To dismiss alerts
driver.find_element(By.ID,"confirmbtn").click()
dismiss_alert = driver.switch_to.alert
print(dismiss_alert.text)
dismiss_alert.dismiss()