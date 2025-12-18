import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\Driver\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkBoxes= driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkBoxes))

for checkBox in checkBoxes:
    if checkBox.get_attribute("value") == "option2":
        checkBox.click()
        assert checkBox.is_selected()
        break
time.sleep(2)

radiobuttons= driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
