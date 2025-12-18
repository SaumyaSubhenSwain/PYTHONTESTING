import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name="Saumya"
service_obj = Service("D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(3)

action = ActionChains(driver)
action.double_click(driver.find_element(By.ID, "checkBoxOption1")).click().perform()
time.sleep(2)
# action.double_click(driver.find_element(By))
# action.context_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
