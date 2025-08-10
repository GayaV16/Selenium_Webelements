import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radio = driver.find_element(By.XPATH,"//input[@value='radio1']")
radio.click()
assert (radio.is_selected())
screenshot_path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\Webpage Elements\\screenshots\\radiobutton.png"
driver.save_screenshot(screenshot_path)